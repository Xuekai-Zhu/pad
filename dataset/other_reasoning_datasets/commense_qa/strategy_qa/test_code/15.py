def solution():
    # Define the weights of a pea and female/male bee hummingbirds
    pea_weight = 0.1
    female_bee_hummingbird_weight = 2.6
    male_bee_hummingbird_weight = 1.95
    # Check if either gender of bee hummingbird could balance the pea on a scale
    if female_bee_hummingbird_weight >= pea_weight or male_bee_hummingbird_weight >= pea_weight:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())