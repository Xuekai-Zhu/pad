def solution():
    """There was a big sale on cat food at the pet store. 20 people bought cat food that day. The first 8 customers bought 3 cases each. The next four customers bought 2 cases each. The last 8 customers of the day only bought 1 case each. How many cases of cat food were sold?"""
    # Calculate the number of cases sold to the first 8 customers
    first_eight = 8 * 3

    # Calculate the number of cases sold to the next 4 customers
    next_four = 4 * 2

    # Calculate the number of cases sold to the last 8 customers
    last_eight = 8 * 1

    # Calculate the total number of cases sold
    total_cases = first_eight + next_four + last_eight

    result = total_cases
    return result

print(solution())