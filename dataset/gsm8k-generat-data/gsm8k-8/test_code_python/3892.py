def solution():
    # Define the number of bags collected by Gina and the neighborhood
    gina_bags = 2
    neighborhood_bags = 82 * gina_bags

    # Calculate the total number of bags collected
    total_bags = gina_bags + neighborhood_bags

    # Calculate the total weight of the litter
    total_weight = total_bags * 4
    result = total_weight
    return result

print(solution())