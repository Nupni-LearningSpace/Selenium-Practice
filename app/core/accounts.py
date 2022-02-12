import json
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(f'{ROOT_DIR}\\..\\data.json', 'r') as myfile:
  data=myfile.read()

# # parse file
accounts = json.loads(data)["accounts"]

def get_acc(acc):
  return accounts[acc]


