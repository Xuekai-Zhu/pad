def solution():
    largest_frog_weight = 120  # The largest frog weighs 120 pounds
    smallest_frog_weight = largest_frog_weight / 10  # The smallest frog weighs 1/10th of the largest frog

    # Calculate the difference in weight between the largest and smallest frog
    weight_difference = largest_frog_weight - smallest_frog_weight
    result = weight_difference
    return result

print(solution())