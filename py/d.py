
s = input()


def convert_to_python_case(text):
    words = text.split('_')
    text = ''.join(word for word in words)
    return text