

def split(array, n):
    for i in range(0, len(array), n):
        yield array[i:i + n]


def split_samples(samples, chunk_len):
    splitted = []
    c = chunk_len - 2
    for s in samples:
        splits = \
            split(s['input_ids'], c), \
            split(s['attention_mask'], c), \
            split(s['offset_mapping'], c), \
            split(s['target_ids'], c)
        for ii, am, om, ti in zip(*splits):
            splitted.append({
                'hash': s['hash'],
                'input_ids': [101, *ii, 102],
                'attention_mask': [1, *am, 1],
                'offset_mapping': [(0, 0), *om, (0, 0)],
                'target_ids': [0, *ti, 0],
            })
    return splitted


def tokenize_targets(tokenizer, tokenizer_defaults, hash, text, selections):
    item = tokenizer.encode_plus(text, **tokenizer_defaults)
    item['hash'] = hash
    item['target_ids'] = []
    p = 0
    for (s, e) in selections:
        if p > s:
            continue
        pre = len(tokenizer.encode_plus(text[p:s], **tokenizer_defaults)['input_ids'])
        item['target_ids'].extend([0] * pre)
        sel = len(tokenizer.encode_plus(text[s:e], **tokenizer_defaults)['input_ids'])
        item['target_ids'].extend([1] * sel)
        p = e
    post = len(tokenizer.encode_plus(text[p:], **tokenizer_defaults)['input_ids'])
    item['target_ids'].extend([0] * post)
    assert len(item['input_ids']) == len(item['target_ids']), 'lengths of source and target are not equal!'
    return item


def preprocess(tokenizer, texts, annotations):

    tokenizer_defaults = {
        'add_special_tokens': False,
        'return_token_type_ids': False,
        'return_offsets_mapping': True,
    }

    samples = []
    for hash, text in texts.items():
        selections = [a for a in annotations if a['policy_hash'] == hash]
        selections = [(int(a['starts_on']), int(a['ends_on'])) for a in selections]
        samples.append(tokenize_targets(tokenizer, tokenizer_defaults, hash, text, selections))

    return split_samples(samples, 512)


def postprocess(dataset, outputs, padding, threshold):
    for i, (d, o) in enumerate(zip(dataset, outputs)):
        dataset[i]['predicted'] = [p['predicted'] for p in o]
        dataset[i]['predicted'], dataset[i]['coords'] = get_coords(d['predicted'], d['offset_mapping'], padding, threshold)
    return dataset


def add_pad(array, pad_item):
    return [pad_item, *array, pad_item]


def merge(array, padding, threshold):
    merged = []
    for i, _ in enumerate(array):
        if sum(array[i-padding:i+padding+1]) / (2 * padding + 1) > threshold:
            merged.append(1)
            continue
        merged.append(0)
    return merged


def boundries(array, coords):
    boundries = []
    start = 0
    for i, d in enumerate(array):
        if d and not start:
            start = coords[i][0]
        if not d and start:
            boundries.append((start, coords[i-1][1]))
            start = 0
    return boundries


def get_coords(data, coords, padding, threshold):
    merged = merge(data, padding, threshold)
    return merged, boundries(add_pad(merged, 0), add_pad(coords, (0, 0)))
