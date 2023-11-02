def solution():
    frankenstein_height = 8 * 12 # convert to inches
    wadlow_height = 8 * 12 + 11.1 # convert to inches
    if wadlow_height > frankenstein_height:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())