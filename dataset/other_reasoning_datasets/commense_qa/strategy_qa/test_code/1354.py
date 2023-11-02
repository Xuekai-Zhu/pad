def solution():
    caesar_children = 3
    khan_children = 16
    khan_probability = 1/200
    khan_descendants = khan_probability * 7.8 * 10 ** 9 # total world population
    if khan_descendants > caesar_children:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())