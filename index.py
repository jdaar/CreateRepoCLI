import configparser

config = configparser.ConfigParser()
config.read('config.ini')

if ('AUTH' not in config.sections()):
    config.add_section('AUTH')
if ('TOKEN' not in config['AUTH']):
    while True:
        AUTH_TOKEN = input('Please enter an authorization token: ')
        if (len(AUTH_TOKEN) > 39):
            break
        else:
            continue
    config['AUTH']['TOKEN'] = AUTH_TOKEN
    with open('config.ini', 'w') as configFile:
        config.write(configFile)
