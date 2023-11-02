def solution():
    total_apples = 85
    wormy_apples = total_apples / 5
    unbruised_apples = total_apples - wormy_apples
    bruised_apples = (1/5 * total_apples) + 9

    # Calculate the number of apples Lex will have left to eat raw
    raw_apples = unbruised_apples - bruised_apples
    result = raw_apples
    return result

print(solution())