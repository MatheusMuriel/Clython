from __future__ import print_function, unicode_literals
from PyInquirer import prompt, Separator
from pprint import pprint

def get_delivery_options(answers):
    options = ['bike', 'car', 'truck']
    if answers['size'] == 'jumbo':
        options.append('helicopter')
    return options
    
questions = [
    {
        'type': 'input',
        'name': 'nome',
        'message': 'Qual é seu nome?',
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
    },
    {
        'type': 'list',
        'name': 'theme',
        'message': 'What do you want to do?',
        'choices': [
            'Order a pizza',
            'Make a reservation',
            Separator(),
            'Ask for opening hours',
            {
                'name': 'Contact support',
                'disabled': 'Unavailable at this time'
            },
            'Talk to the receptionist'
        ]
    },
    {
        'type': 'list',
        'name': 'size',
        'message': 'What size do you need?',
        'choices': ['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'delivery',
        'message': 'Which vehicle you want to use for delivery?',
        'choices': get_delivery_options,
    },
]

answers = prompt(questions)

pprint(answers)
print('Seu nome é', answers['nome'])
print('Você escolheu', answers['fruta'])