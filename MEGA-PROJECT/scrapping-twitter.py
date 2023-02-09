import os 
import twint
import numpy as np
import pandas as pd

# dirpath = os.path.dirname(os.path.realpath(__file__)) 

def twint_search(search, name_file, lang = 'id', limit = 10):
    config = twint.Config()
    config.Search = search
    config.Lang = lang
    config.Limit = limit
    config.Store_csv = True
    config.Output(name_file)

    twint.run.Search(config)


    # return config.output()

test_search = twint_search('islam', 'store_twit_islam.csv')
# print(dirpath)
# print(test_search)
