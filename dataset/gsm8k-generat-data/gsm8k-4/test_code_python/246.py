def solution():
    """The ratio of boys to girls in a family is 5:7. The total number of children in the family is 180. If the boys are given $3900 to share, how much money does each boy receive?"""
    # Define the ratio of boys to girls
    boy_to_girl_ratio = 5/7

    # Calculate the total number of children in the family
    total_children = 180

    # Calculate the number of boys in the family
    total_boys = total_children / (1 + boy_to_girl_ratio)

    # Calculate the amount of money each boy receives
    amount_per_boy = 3900 / total_boys

    result = amount_per_boy
    return result

print(solution())