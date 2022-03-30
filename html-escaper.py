#make a program able to convert a user inserted string to an html valid one
args = input('Enter a string: ')

def char_converter(element):
    if element == '<':
        element = '&lt;'
    elif element == '>':
        element = '&gt;'
    elif element == '&':
        element = '&amp;'
    elif element == '"':
        element = '&quot;'
    return element

def html_converter(string):
    for element in string:
        print(char_converter(element), end ="")

html_converter(args)

exit

