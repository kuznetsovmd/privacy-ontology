from ontology2.interface import Ontology


def process_onto_test():

    o = Ontology('test', 'some url')

    fp = o.individual('FirstParty')
    u = o.individual('User')


    o.individual(

        'FPCollection',

        binds=[
            o.property('initiated_by', fp),
            o.property('collects', u),
            o.property('has_mechanism', o.individual('Email')),
        ]
    )

    o.individual(

        'UserNotification',

        binds=[
            o.property('initiated_by', u),
            o.property('notifies', fp),
            o.property('has_mechanism', o.individual('Email')),
        ]
    )

    o.individual(

        'FPNotification',

        binds=[
            o.property('initiated_by', fp),
            o.property('notifies', u),
            o.property('has_mechanism', o.individual('Email')),
        ]
    )

    o.save()
