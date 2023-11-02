def solution():
    """The ratio of boys to girls in a family is 5:7. The total number of children in the family is 180. If the boys are given $3900 to share, how much money does each boy receive?"""
    # Define the ratio of boys to girls
    BOYS_TO_GIRLS = 5/7

    # Calculate the total number of children
    total_children = 180

    # Calculate the number of boys
    boys = total_children / (1 + BOYS_TO_GIRLS)

    # Calculate the amount of money each boy receives
    each_boy = 3900 / boys

    # Display the amount of money each boy receives
    result = each_boy
    return result

print(solution())