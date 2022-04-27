import os

# Глобал хувьсагч
Codes = dict()

class Node(object):
    
    # Байгуулагч функц
    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.Code = ''

# Өгөгдлийн давтамжийг тоолох
def calculate_prob(data):
    symbols = dict()
    for elements in data:
        if symbols.get(elements) == None:
            symbols[elements] = 1
        else:
            symbols[elements] += 1
    return symbols


def calculate_codes(node, val=''):
    newVal = val + str(node.Code)
    if(node.left):
        calculate_codes(node.left, newVal)
    if(node.right):
        calculate_codes(node.right, newVal)
    if (not node.left and not node.right):
        Codes[node.symbol] = newVal

# Encoded String
def output_encoded(data, coding):
    encoding_output = []
    for idx in data:
        encoding_output.append(coding[idx])
    string_dat = ''.join([str(item) for item in encoding_output])
    return string_dat