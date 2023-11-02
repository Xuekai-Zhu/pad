def solution():
    """ Mr. Rainwater has some goats, 9 cows and some chickens.
    He has 4 times as many goats as cows and 2 times as many goats as chickens.
    How many chickens does he have? """
    
    # Define the number of cows
    cows = 9
    
    # Define the number of goats
    goats = cows * 4
    
    # Define the number of chickens
    chickens = goats / 2
    
    # Display the number of chickens
    result = chickens
    return result

print(solution())