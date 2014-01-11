import sys
import os
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types

# TODO: Get rid of __file__ by using modules
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def run():
    # Creating instance of EvernoteClient    
    f = open(BASE_PATH + '/dev_token', 'r')
    dev_token = f.read()
    client = EvernoteClient(token=dev_token)
    f.close()

    # Getting instance of userStore.
    # Getting instance of user - This contains the accounts details of the user
    userStore = client.get_user_store()
    user = userStore.getUser()
    print("Username: " + user.username)

    # Getting instance of noteStore
    noteStore = client.get_note_store()
    notebooks = noteStore.listNotebooks()
    print("Notebooks: ")
    for n in notebooks:
        print "-" + n.name

if __name__ == "__main__":
    print("Running on python version" + sys.version)
    run()