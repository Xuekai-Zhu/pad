def solution():
    """If a tarantula has eight legs, and one tarantula egg sac can contain 1000 tarantulas, how many baby tarantula legs would be in one less than 5 egg sacs?"""
    # Define the number of egg sacs
    egg_sacs = 4
    
    # Calculate the total number of tarantulas
    total_tarantulas = egg_sacs * 1000
    
    # Calculate the total number of tarantula legs
    total_legs = total_tarantulas * 8
    
    # Calculate the number of baby tarantula legs in one less than 5 egg sacs
    baby_legs = (egg_sacs - 1) * 1000 * 8
    
    # return the result
    result = baby_legs
    return result

print(solution())