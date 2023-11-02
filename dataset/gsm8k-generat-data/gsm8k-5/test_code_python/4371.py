def solution():
    total_candy = 63  # Jerry had 63 pieces of candy
    num_bags = 9  # Jerry divided the candy equally into 9 bags

    # Calculate how many pieces of candy were in each bag
    candy_per_bag = total_candy / num_bags

    # Calculate how many bags had chocolate hearts
    num_hearts_bags = 2
    total_hearts = num_hearts_bags * candy_per_bag

    # Calculate how many bags were chocolate kisses
    num_kisses_bags = 3
    total_kisses = num_kisses_bags * candy_per_bag

    # Calculate how many pieces of candy were not chocolate
    not_chocolate = total_candy - total_hearts - total_kisses
    result = not_chocolate
    return result

print(solution())