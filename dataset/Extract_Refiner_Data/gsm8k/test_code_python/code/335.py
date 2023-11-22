def solution():
    
    # Define the number of animals and the ratio of chickens to cows
    total_animals = 60
    chicken_to_cow_ratio = 2

    # Calculate the number of chickens and cows
    total_chickens = total_animals * chicken_to_cow_ratio
    total_cows = total_animals / (1 + chicken_to_cow_ratio)

    # Calculate the total number of legs
    total_legs = total_chickens * 4

    # Display the total number of legs
    result = total_legs
    return result

print(solution())