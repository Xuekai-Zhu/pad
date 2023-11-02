def solution():
    
    # Define the initial number of cows and chickens
    initial_cows = 50
    initial_chickens = 20

    # Calculate the number of cows and chickens after three weeks
    cows_after_three_weeks = initial_cows - (20 * 7)
    chickens_after_three_weeks = initial_chickens - (10 * 7)

    # Calculate the total number of animals after three weeks
    total_animals = cows_after_three_weeks + chickens_after_three_weeks

    # return the result
    result = total_animals
    return result

print(solution())