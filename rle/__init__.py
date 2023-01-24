def encode(string):
    
    encoded = ''
    counter = 1
    string += '\0'

    for i, (a, b) in enumerate(zip(string[: -1], string[1 :])):

        if a == b:
            counter += 1

        else:
            code = f'{count}{a}'

            if len(code) < counter:
                encoding += code
            
            else:
                encoding += a

            counter = 1
    
    return encoding
