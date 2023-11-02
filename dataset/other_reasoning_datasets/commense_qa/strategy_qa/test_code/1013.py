def solution():
    eighth_amendment = "prohibits excessive bail, fines, and cruel punishments"
    first_amendment = "protects freedom of speech"
    if "freedom of speech" not in eighth_amendment:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())