def solution():
    """There was a big sale on cat food at the pet store. 20 people bought cat food that day. The first 8 customers bought 3 cases each. The next four customers bought 2 cases each. The last 8 customers of the day only bought 1 case each. How many cases of cat food were sold?"""
    # Define the number of cases bought by each group of customers
    group_1 = 3
    group_2 = 2
    group_3 = 1

    # Define the number of customers in each group
    group_1_customers = 8
    group_2_customers = 4
    group_3_customers = 8

    # Calculate the total number of cases bought
    total_cases = (group_1 * group_1_customers) + (group_2 * group_2_customers) + (group_3 * group_3_customers)

    # Display the total number of cases bought
    result = total_cases
    return result

print(solution())