def solution():
    """There was a big sale on cat food at the pet store. 20 people bought cat food that day. The first 8 customers bought 3 cases each. The next four customers bought 2 cases each. The last 8 customers of the day only bought 1 case each. How many cases of cat food were sold?"""
    first_group = 8 * 3
    second_group = 4 * 2
    third_group = 8 * 1
    total_cases_sold = first_group + second_group + third_group
    result = total_cases_sold
    return result

print(solution())