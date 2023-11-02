def solution():
    initial_rice = 50  # Mr. Llesis had 50 kilograms of rice
    stored_rice = initial_rice * (7/10)  # Mr. Llesis kept 7/10 of the rice
    given_rice = initial_rice - stored_rice  # Mr. Llesis gave the rest to Mr. Everest

    # Calculate the difference between the amount of rice Mr. Llesis kept and Mr. Everest received
    difference = stored_rice - given_rice
    result = difference
    return result

print(solution())