def solution():
    total_decorations = 15 / (1 - (2/3) - (2/5)) # calculate the total number of decorations
    nails_used = (2/3) * total_decorations # calculate the number of decorations that used nails
    result = nails_used
    return result

print(solution())