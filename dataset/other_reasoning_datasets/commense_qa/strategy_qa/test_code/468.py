def solution():
    nolan_height = 6*12 # Convert height in feet to inches
    devito_height = 4*12 + 10 # Convert height in feet and inches to inches
    if nolan_height <= devito_height:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())