from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pprint import pprint
questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'Whats your first name',
    },
    {
        'type': 'list',
        'name': 'fruta',
        'message': 'Escolha uma fruta',
        'choices': [
            'Banana',
            'Maça',
            'Abacaxi',
            'Tomate?'
        ]
    }
]
answers = prompt(questions)
pprint(answers)

print('Você escolheu', answers['fruta'])