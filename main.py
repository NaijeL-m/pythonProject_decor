import csv
import requests
import time
import datetime

def path_logg(path):
    def dec_logg(func):
        def new_res(*args, **kwargs):
            res = func(*args, **kwargs)
            result_list = [datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S"), func.__name__, *args, {**kwargs}, res]
            with open(path+"filebook.csv", "r+") as f:
                f.seek(0, 2)
                datawriter = csv.writer(f, delimiter=',')
                datawriter.writerows([result_list])
            return res
        return new_res
    return dec_logg

@path_logg("to/")
def intel(list_some):
    f = ""
    for i in list_some:
        f += i
    return f

def intellectus(list_hero):
    max=[0, ""]
    for hero in list_hero:
        x = requests.get('https://superheroapi.com/api/2619421814940190/search/'+hero)
        intell=int(x.json()['results'][0]['powerstats']['intelligence'])
        if intell > max[0]:
            max[0] = intell
            max[1] = hero
    return max[1]
s = ['Hulk', 'Captain America', 'Thanos']
t = ['Spider-man', 'Ant-man']
print(intel(s))
print(intel(t))

