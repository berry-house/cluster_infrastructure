# /usr/bin/python2.7
from base64 import b64encode as encode
import json
from os import listdir, remove
from sys import argv


def build_broker(database, username, password):
    template = open('kubernetes/broker.yaml.template', 'r').read()
    with open('kubernetes/broker.yaml', 'w') as f:
        f.write(template % (encode(database), encode(username), encode(password)))

def build_database():
    template = open('kubernetes/database.yaml.template', 'r').read()
    with open('kubernetes/database.yaml', 'w') as f:
        f.write(template)

def build_client(database, username, password):
    template = open('kubernetes/client.yaml.template', 'r').read()
    with open('kubernetes/client.yaml', 'w') as f:
        f.write(template % (encode(database), encode(username), encode(password)))

def clean():
    files = listdir('kubernetes/')

    for f in files:
        if f.endswith(".yaml"):
            remove('kubernetes/%s' % f)

def main():
    if len(argv) < 2:
        print 'Argument must be passed (either clean or build)'
        exit()

    if argv[1] == 'clean':
        clean()
    elif argv[1] == 'build' and len(argv) == 3:
        data = json.load(open(argv[2]))

        build_database()
        build_broker(data['broker']['database'], data['broker']['username'], data['broker']['password'])
        build_client(data['client']['database'], data['client']['username'], data['client']['password'])

    else:
        print 'Invalid mode'

if __name__ == '__main__':
    main()
