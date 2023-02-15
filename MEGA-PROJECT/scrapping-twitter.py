import os
import twint
import numpy as np
import pandas as pd

# dirpath = os.path.dirname(os.path.realpath(__file__))


def twint_search(search, name_file, lang='en', limit=10, store=True):
    config = twint.Config()
    config.Search = search
    config.Lang = lang
    config.Limit = limit
    config.Store_csv = store
    config.Output = name_file

    twint.run.Search(config)

    # return config.output()


keyword = 'jokowi'
# test_search = twint_search('islam', 'store_twit_islam.json', store = True, limit = 10000)
twint_search(
    keyword, 'databases/store_twit_{}.csv'.format(keyword), limit=20000)
# print(dirpath)
# print(test_search)
