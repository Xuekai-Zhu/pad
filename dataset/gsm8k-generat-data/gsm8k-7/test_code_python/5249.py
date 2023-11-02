def solution():
    num_children = 2
    num_holidays_per_child = 4
    num_holidays_for_husband = 6
    num_holidays_for_parents = 2
    num_years = 10

    # Calculate the total number of cakes for her children
    total_cakes_for_children = num_children * num_holidays_per_child * num_years

    # Calculate the total number of cakes for her husband
    total_cakes_for_husband = num_holidays_for_husband * num_years

    # Calculate the total number of cakes for her parents
    total_cakes_for_parents = num_holidays_for_parents * num_years

    # Calculate the total number of cakes she makes in 10 years
    total_cakes = total_cakes_for_children + total_cakes_for_husband + total_cakes_for_parents
    result = total_cakes
    return result

print(solution())