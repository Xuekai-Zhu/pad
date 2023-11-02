def solution():
    """Out of the 120 people who attended the party, 1/3 are men while half are women. The rest are children. How many children attended the party?"""
    # Define the total number of people and the number of men and women
    total_people = 120
    men = total_people // 3
    women = total_people // 2

    # Calculate the number of children
    children = total_people - men - women

    # Return the result
    result = children
    return result

print(solution())