from ontology2.ontology.interface import Ontology


def process_onto_examples():

    o = Ontology('test', 'some url')

    fp = o.individual('FirstParty')
    u = o.individual('User')
    email = o.individual('OnWebsitePage')


    o.individual(

        'FPCollection',

        binds=[
            o.property('initiated_by', fp),
            o.property('collects', u),
            o.property('has_mechanism', email),
        ]
    )

    o.individual(

        'UserNotification',

        binds=[
            o.property('initiated_by', u),
            o.property('notifies', fp),
            o.property('has_mechanism', email),
        ]
    )

    o.individual(

        'FPNotification',

        binds=[
            o.property('initiated_by', fp),
            o.property('notifies', u),
            o.property('has_mechanism', email),
        ]
    )

    o.save()