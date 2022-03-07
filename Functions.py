def IntConvert(Input):
    X = Input[::-1].lstrip("0")[::-1]
    if X != '':
        return int(X, 16)
    else:
        return 0
