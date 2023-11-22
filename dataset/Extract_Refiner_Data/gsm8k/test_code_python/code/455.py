def solution():
    
    # Define the weight of each type of horse
    sugar_box_weight = 1
    carrot_bag_weight = 12
    hay_weight = 75
    oats_weight = 25

    # Define the number of each type of horse purchased
    sugar_cubes = 2
    hay_bags = 4
    oats_bags = 2

    # Calculate the total weight of the horses purchased
    total_weight = (sugar_box_weight * sugar_cubes) + (hay_bags * hay_bags) + (oats_bags * oats_weight)

    # Display the total weight
    result = total_weight
    return result

print(solution())