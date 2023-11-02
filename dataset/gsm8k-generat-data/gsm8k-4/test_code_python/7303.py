def solution():
    """Mr. Llesis had 50 kilograms of rice. He kept 7/10 of it in storage and gave the rest to Mr. Everest. How many kilograms of rice did Mr. Llesis keep than Mr. Everest?"""
    # Define the initial amount of rice Mr. Llesis had
    initial_rice = 50

    # Calculate the amount of rice Mr. Llesis kept in storage
    rice_in_storage = initial_rice * (7/10)

    # Calculate the amount of rice Mr. Llesis gave to Mr. Everest
    rice_to_everest = initial_rice - rice_in_storage

    # Calculate the difference between the amount of rice Mr. Llesis kept and the amount given to Mr. Everest
    difference = rice_in_storage - rice_to_everest

    # Return the difference in kilograms
    result = difference
    return result

print(solution())