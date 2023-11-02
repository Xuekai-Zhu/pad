def solution():
    atlantic_border = True
    pacific_border = True
    indian_border = False
    if atlantic_border or pacific_border or indian_border:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())