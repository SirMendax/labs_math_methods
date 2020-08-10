
def unique_in_order(iterable):
    symbols = []
    for char in iterable:
        if len(symbols) == 0:
            symbols.append(char)
        else:
            if char != symbols[-1]:
                symbols.append(char)
    return symbols
