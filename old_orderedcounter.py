from collections import Counter, OrderedDict


# this is a snippet somebody posted on discord for an 'Ordered Counter'

# It's a useful piece of Python code (until all dictionaries became ordered)
# it defines the class OrderedCounter by perfectly merging Counter and OrderedDict:

class OrderedCounter(Counter, OrderedDict):
    pass

# [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
