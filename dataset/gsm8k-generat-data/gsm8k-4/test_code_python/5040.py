def solution():
    """There are 320 ducks in a pond. On the first night 1/4 of them get eaten by a fox. On the second night 1/6 of the remaining ducks fly away, and on the third night 30 percent are stolen. How many ducks remain after the three nights?"""
    # Define the initial number of ducks and the number that get eaten by a fox on the first night
    initial_ducks = 320
    first_night_loss = initial_ducks * (1/4)

    # Calculate the number of ducks remaining after the first night
    remaining_ducks = initial_ducks - first_night_loss

    # Calculate the number of ducks that fly away on the second night
    second_night_loss = remaining_ducks * (1/6)

    # Calculate the number of ducks remaining after the second night
    remaining_ducks = remaining_ducks - second_night_loss

    # Calculate the number of ducks stolen on the third night
    third_night_loss = remaining_ducks * 0.3

    # Calculate the final number of ducks remaining
    final_ducks = remaining_ducks - third_night_loss

    # Return the result
    result = final_ducks
    return result

print(solution())