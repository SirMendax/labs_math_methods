def decoder(word):
    symbol = ''
    decoding_word = ''
    for char in word.strip() + 's':
        if char == ' ' or char == 's':
            decoding_word += MORSE_CODE[symbol]
            symbol = ''
        else:
            symbol += char
    return decoding_word

def decodeMorse(morse_code):
    morse_code = morse_code.strip().split('  ')
    result = ''

    for word in morse_code:
        if morse_code[-1] == word:
            result += decoder(word)
        else:
            result += decoder(word) + ' '
    return result



============
def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))
