def rainbow(text):
    returntext = ''
    colors = ['\033[91m', '\033[93m', '\033[94m',
              '\033[92m', '\033[95m', '\033[96m', '\033[97m']
    for i in range(len(text)):
        returntext += (colors[i % len(colors)] + text[i])
    returntext += ('\033[0m')
    return returntext


userInput = input("Enter a string to rainbow: ")
print(rainbow(userInput))
