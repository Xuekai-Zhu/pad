def solution():
    # Calculate the number of boys and girls in the family
    total_ratio = 5 + 7
    boys_ratio = 5 / total_ratio
    girls_ratio = 7 / total_ratio
    total_children = 180
    number_of_boys = boys_ratio * total_children

    # Calculate the amount of money each boy receives
    amount_per_boy = 3900 / number_of_boys
    result = amount_per_boy
    return result

print(solution())