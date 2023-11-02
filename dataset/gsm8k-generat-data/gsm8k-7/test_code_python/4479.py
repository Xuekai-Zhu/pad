def solution():
    total_bushels = 50
    terry_bushels = 8
    jerry_bushels = 3
    linda_bushels = 12
    stacy_ears = 21
    ears_per_bushel = 14

    # Calculate the total number of ears of corn
    total_ears = total_bushels * ears_per_bushel

    # Calculate the number of ears of corn given away
    given_away_ears = (terry_bushels + jerry_bushels + linda_bushels) * ears_per_bushel + stacy_ears

    # Calculate the number of ears of corn left
    left_ears = total_ears - given_away_ears
    result = left_ears
    return result

print(solution())