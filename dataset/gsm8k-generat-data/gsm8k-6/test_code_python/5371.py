def solution():
    # Calculate the number of apples James got
    james_apples = 5 + 2  # James got 2 more apples than Jane

    # Calculate the total number of apples given away
    total_given_away = 5 + james_apples

    # Calculate the remaining apples
    remaining_apples = 20 - total_given_away

    # Calculate the number of apples Martha still needs to give away
    apples_to_give_away = remaining_apples - 4

    result = apples_to_give_away
    return result

print(solution())