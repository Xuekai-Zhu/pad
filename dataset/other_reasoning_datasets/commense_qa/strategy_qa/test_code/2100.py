def solution():
    second_row = "QWERTYUIOP"
    kingdom_name = "ABDASTARTUS"
    for letter in kingdom_name:
        if letter not in second_row:
            result = "no"
            break
    else:
        result = "yes"
    return result

print(solution())