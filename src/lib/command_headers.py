from src.config.config import *

commands = {
    '!test': {
        'limit': 30,
        'return': 'This is a test!'
    },

    '!randomemote': {
        'limit': 5,
        'argc': 0,
        'return': 'command'
    },

    '!song': {
        'limit':5,
        'argc':1,
        'return':'command'
    },

    '!stats': {
        'limit': 5,
        'argc': 1,
        'return': 'command'
    }
}

for channel in config['channels']:
    for command in commands:
        commands[command][channel] = {}
        commands[command][channel]['last_used'] = 0
