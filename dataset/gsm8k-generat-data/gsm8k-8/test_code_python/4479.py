def solution():
    # Calculate the total number of ears of corn in the 50 bushels
    total_corn = 50 * 14

    # Calculate the number of ears of corn given away
    given_away = 8 + 3 + 12 + 21

    # Calculate the number of ears of corn remaining
    remaining_corn = total_corn - given_away

    result = remaining_corn
    return result

print(solution())