def solution():
    # Define the number of lemons in a dozen
    lemons_in_dozen = 12

    # Calculate the total number of lemons Cristine had
    total_lemons = lemons_in_dozen

    # Calculate the number of lemons Cristine gave away
    lemons_given_away = total_lemons / 4

    # Calculate the number of lemons Cristine has left
    lemons_left = total_lemons - lemons_given_away

    result = lemons_left
    return result

print(solution())