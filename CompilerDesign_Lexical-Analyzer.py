import re

# Dictionaries for token identification
operators = {'=': 'Assignment op', '+': 'Addition op', '-': 'Subtraction op', '/': 'Division op',
             '*': 'Multiplication op', '<': 'Less-than op', '>': 'Greater-than op'}

data_type = {'int': 'integer type', 'float': 'Floating point', 'char': 'Character type', 'long': 'long int'}

terminator = {':': 'colon', ';': 'semi-colon', '.': 'dot', ',': 'comma'}

condition = {'if': 'If Condition', 'else': 'Else condition', 'elif': 'Else-If Condition'}

identifier = {'a': 'id', 'b': 'id', 'x': 'id', 'y': 'id'}


# Analyzer Function
def lexical_analyzer(inp_string):
    count = 0
    program = inp_string.split("\n")

    tokens = inp_string.split(' ')
    print("Tokens are ", tokens)
    for token in tokens:
        if token in operators:
            print("Operator is ", operators[token])
        elif token in data_type:
            print("Datatype is", data_type[token])
        elif token in terminator:
            print(token, terminator[token], "is a Terminator symbol")
        elif token in condition:
            print("Condition is", condition[token])
        elif token in identifier:
            print(identifier[token], token, "Is an Identifier", )
        elif token.isnumeric():
            print(token, "is a number")
    dataFlag = False
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _")

# Input String Used: int x = 10 ; if(x > 5) { return x ; } else { return 0 ; }
prompt = input(print("Enter String"))
print(lexical_analyzer(prompt))

# ****Output****
# Tokens are
# ['int', 'x', '=', '10', ';', 'if(x', '>', '5)', '{', 'return', 'x', ';', '}', 'else', '{', 'return', '0', ';', '}']
# Datatype is integer type
# id x Is an Identifier
# Operator is  Assignment op
# 10 is a number
# ; Terminator symbol is semi-colon
# Operator is  Greater-than op
# id x Is an Identifier
# ; Terminator symbol is semi-colon
# Condition is Else condition
# 0 is a number
# ; Terminator symbol is semi-colon
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _
