def solution():
    gina_bags = 2
    neighborhood_bags = 82 * gina_bags
    bag_weight = 4 # in pounds

    # Calculate the total weight of litter collected by Gina and the neighborhood
    total_weight = (gina_bags + neighborhood_bags) * bag_weight
    result = total_weight
    return result

print(solution())