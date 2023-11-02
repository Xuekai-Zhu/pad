def solution():
    city = "Aurangabad"
    state = "Maharashtra"
    language_spoken = "Marathi"
    fluent_in_language = True
    if city in state.lower() and language_spoken.lower() == "marathi" and fluent_in_language:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())