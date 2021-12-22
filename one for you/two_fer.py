def two_fer(name = ""):

    if len(name) > 0:
        sentence = "One for you, one for me.".replace("you", name)
    else:
        sentence = "One for you, one for me."

    return sentence
