def solution():
    """Antoine is having a dinner party and his butcher recommends 1/2 pound of meat per person. If he's inviting 6 people over and the beef tenderloin is $15.00 a pound, how much will this cost him?"""
    # Define the recommended amount of meat per person
    MEAT_PER_PERSON = 0.5

    # Define the number of guests
    guests = 6

    # Define the price per pound of beef tenderloin
    PRICE_PER_POUND = 15.0

    # Calculate the total amount of meat needed
    total_meat = guests * MEAT_PER_PERSON

    # Calculate the total cost of the beef tenderloin
    total_cost = total_meat * PRICE_PER_POUND

    # return the result
    result = total_cost
    return result

print(solution())