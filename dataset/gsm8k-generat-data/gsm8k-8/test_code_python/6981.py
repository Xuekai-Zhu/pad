def solution():
    #Define the initial number of candies
    initial_candies = 100
    #Define the number of candies daughter eats
    daughter_candies = 8
    #Define the remaining candies
    remaining_candies = initial_candies - daughter_candies
    #Define the number of bowls
    num_bowls = 4
    #Define the candies per bowl
    candies_per_bowl = (remaining_candies // num_bowls) - 3
    result = candies_per_bowl
    return result

print(solution())