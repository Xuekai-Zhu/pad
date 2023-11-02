def solution():
    """There are 45 children in a classroom. One-third of them are girls. How many boys are in the classroom?"""
    # Define the total number of children and the ratio of girls to total
    total_children = 45
    girls_ratio = 1/3

    # Calculate the number of girls and boys
    girls = total_children * girls_ratio
    boys = total_children - girls

    # return the number of boys
    result = boys
    return result

print(solution())