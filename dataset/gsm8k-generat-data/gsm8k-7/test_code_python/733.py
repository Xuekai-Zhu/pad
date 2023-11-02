def solution():
    henry_shells = 11
    paul_shells = 24
    initial_total = 59

    # Calculate Leo's initial collection by subtracting Henry and Paul's collections from the initial total
    leo_shells = initial_total - henry_shells - paul_shells

    # Calculate the number of shells Leo gave away
    leo_given_away = leo_shells / 4

    # Calculate the total number of shells they have now
    total_shells = initial_total - leo_given_away
    result = total_shells
    return result

print(solution())