def solution():
    total_candy = 63
    num_bags = 9
    num_choco_hearts = 2
    num_choco_kisses = 3

    # Calculate the total number of chocolate candies
    total_choco_candy = num_choco_hearts + num_choco_kisses

    # Calculate the total number of non-chocolate candies
    non_choco_candy = total_candy - total_choco_candy

    # Calculate the number of non-chocolate candies in each bag
    non_choco_per_bag = non_choco_candy / (num_bags - total_choco_candy)

    result = non_choco_per_bag
    return result

print(solution())