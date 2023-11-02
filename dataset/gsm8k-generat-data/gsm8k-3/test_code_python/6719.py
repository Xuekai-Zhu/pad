def solution():
    """There are 45 children in a classroom. One-third of them are girls. How many boys are in the classroom?"""
    # Define the total number of children and the fraction that are girls
    total_children = 45
    girls_fraction = 1/3

    # Calculate the number of girls and boys
    girls = total_children * girls_fraction
    boys = total_children - girls

    # Display the number of boys
    result = boys
    return result

print(solution())