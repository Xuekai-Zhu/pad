def solution():
    # Define the variables
    meat_weight = 10  # in pounds
    num_links = 40
    eaten_links = 12
    remaining_links = num_links - eaten_links

    # Calculate the weight per link in ounces
    weight_per_link = meat_weight * 16 / num_links

    # Calculate the total weight of the remaining links in ounces
    remaining_weight = remaining_links * weight_per_link

    # Return the remaining weight in ounces
    result = remaining_weight
    return result

print(solution())