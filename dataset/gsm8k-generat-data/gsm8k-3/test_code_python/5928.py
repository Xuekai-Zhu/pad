def solution():
    """Three companies, A, B, and C, each purchased 10 ad spaces on a newspaper, with each ad space having a size of 12 foot by 5-foot rectangle. If each square foot ad was charged at $60, how much money did the three pay for the ads combined?"""
    # Define the size of each ad space
    AD_WIDTH = 12
    AD_HEIGHT = 5
    AD_SIZE = AD_WIDTH * AD_HEIGHT

    # Define the number of ad spaces purchased by each company
    a_spaces = 10
    b_spaces = 10
    c_spaces = 10

    # Calculate the total area of all ad spaces
    total_area = (a_spaces + b_spaces + c_spaces) * AD_SIZE

    # Calculate the total cost of all the ads
    total_cost = total_area * 60

    # Display the total cost
    result = total_cost
    return result

print(solution())