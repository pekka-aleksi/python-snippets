import re
from math import sqrt

# this was a homework exercise for somebody on discord
# it seemed fun so I implemented

laws = {
    'ohms': {
        'U': lambda x: x['I'] * x['R'],
        'I': lambda x: x['U'] / x['R'],
        'R': lambda x: x['U'] / x['I']},
    'pythagoras': {
        'A': lambda x: sqrt(x['B'] ** 2 - x['C'] ** 2),
        'B': lambda x: sqrt(x['C'] ** 2 - x['A'] ** 2),
        'C': lambda x: sqrt(x['A'] ** 2 + x['B'] ** 2)
    },
    'kinematics': {
        'S': lambda x: x['V'] * x['T'],
        'V': lambda x: x['S'] / x['T'],
        'T': lambda x: x['S'] / x['V']
    }
}

regex_value = r'\b\w+\:\d+\b'  # the regex is used to parse the "i:3" and "r:10" parts from the strings

for test in ['i:3 r:10', 'a:3 b:4', 's:5 t:10']:

    # we loop over three test inputs here which test each of three functions defined above.

    # INPUT = input()
    INPUT = test

    found_variables = dict()

    for found_input in re.findall(regex_value, INPUT):
        var_name, var_value = found_input.upper().split(':')  # we split the "i:3" into name := value
        found_variables[var_name] = float(var_value)  # then store them into a dictionary

    for law_name, law_specifics in laws.items():

        law_variables = law_specifics.keys()
        missing_vars = set(law_variables) - set(found_variables)

        if len(missing_vars) == 1:
            the_missing_variable = missing_vars.pop()
            print(f"{law_name} laws is missing variable: {the_missing_variable}")

            function = law_specifics[the_missing_variable]
            print(f"The value of the function is {function(found_variables)}")

    print("-" * 80)
