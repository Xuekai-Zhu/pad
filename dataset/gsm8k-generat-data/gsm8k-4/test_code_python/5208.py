def solution():
    """A group of people pays $720 for admission tickets to an amusement park. The price of an adult ticket is $15, and a child ticket is $8. There are 25 more adults than children. How many children are in the group?"""
    # Define the total amount paid and the price per ticket
    total_paid = 720
    adult_price = 15
    child_price = 8

    # Define the difference in number between adults and children
    difference = 25

    # Set up the equations to solve for the number of adults and children
    # Let A be the number of adults and C be the number of children
    # A + C = total_people
    # A - C = difference

    # Adding the above two equations, we get:
    # 2A = total_people + difference
    # A = (total_people + difference)/2

    # Subtracting the second equation from the first, we get:
    # 2C = total_people - difference
    # C = (total_people - difference)/2

    total_people = (total_paid / adult_price + total_paid / child_price) / 2
    children = (total_people - difference) / 2

    result = children
    return result

print(solution())