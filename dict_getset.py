class OverrideDict(dict):
    def __getitem__(self, key):
        l, r = str(key).split('/')
        lval = dict.__getitem__(self, l)
        rval = dict.__getitem__(lval, r)
        return rval

    def __setitem__(self, key, val):
        l, r = str(key).split('/')
        litem = dict.__getitem__(self, l)
        dict.__setitem__(litem, r, val)


v = OverrideDict(
    {"A": 34,
     "B": {
         "C": 1,
         "D": "x"
     }
     })

print(v['B/C'])
v['B/Y'] = 1000

print(v)
