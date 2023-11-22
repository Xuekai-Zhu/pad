def solution():
    
    # Define the weight of each flower
    rose_weight = 1
    carnation_weight = 1.5
    sunflower_weight = 3

    # Define the number of flowers planted
    num_sunflowers = 4
    num_carnations = 10

    # Calculate the total weight of the soil
    total_weight = num_sunflowers * sunflower_weight + num_carnations * carnation_weight

    # Calculate the number of roses that can be planted
    num_roses = total_weight // rose_weight

    # return the result
    result = num_roses
    return result

print(solution())