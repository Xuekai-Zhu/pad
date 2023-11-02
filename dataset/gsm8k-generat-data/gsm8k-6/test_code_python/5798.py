def solution():
    total_apples = 85  # total number of apples picked by Lex
    wormy_apples = total_apples / 5  # number of apples with worms
    bruised_apples = (1/5 * total_apples) + 9  # number of bruised apples
    raw_apples = total_apples - wormy_apples - bruised_apples  # number of apples left to eat raw
    result = raw_apples
    return result

print(solution())