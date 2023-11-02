def solution():
    phrase = "Lorem ipsum"
    backwards = phrase[::-1] # reversing the string
    first_letters = [word[0].lower() for word in backwards.split()]
    if len(set(first_letters)) == 1: # check if all first letters are the same
        result = "yes"
    else:
        result = "no"
    return result

print(solution())