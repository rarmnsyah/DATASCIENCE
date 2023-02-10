import os 
import twint
import numpy as np
import pandas as pd

# dirpath = os.path.dirname(os.path.realpath(__file__)) 

def twint_search(search, name_file, lang = 'id', limit = 10, store = False):
    config = twint.Config()
    config.Search = search
    config.Lang = lang
    config.Limit = limit
    config.Store_json = store
    config.Output = name_file

    twint.run.Search(config)


    # return config.output()

test_search = twint_search('islam', 'store_twit_islam.json', store = True, limit = 10000)
# print(dirpath)
# print(test_search)
