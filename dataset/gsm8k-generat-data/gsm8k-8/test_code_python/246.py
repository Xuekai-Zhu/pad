def solution():
    # Define the ratio of boys to girls
    boys_to_girls_ratio = 5/7

    # Calculate the total number of children
    total_children = 180

    # Calculate the number of boys and girls
    total_ratio = 5 + 7
    num_boys = total_children * (5/total_ratio)
    num_girls = total_children * (7/total_ratio)

    # Calculate the amount of money each boy receives
    amount_per_boy = 3900 / num_boys
    result = amount_per_boy
    return result

print(solution())