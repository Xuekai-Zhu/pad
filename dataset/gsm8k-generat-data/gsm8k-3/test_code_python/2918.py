def solution():
    """Monica charges $25.00 per person when catering a dinner party.  For repeat customers, she offers a 10% discount.  Phoebe is a repeat customer who is having a dinner party for 20 guests.  How much will Monica make from the party?"""
    # Define the price per person and discount rate
    PRICE_PER_PERSON = 25
    DISCOUNT_RATE = 0.1

    # Define the number of guests and whether the customer is a repeat customer
    num_guests = 20
    repeat_customer = True

    # Calculate the total cost before any discounts
    total_cost = num_guests * PRICE_PER_PERSON

    # Apply the repeat customer discount if applicable
    if repeat_customer:
        discount = total_cost * DISCOUNT_RATE
        total_cost -= discount

    # Display the total cost to Monica
    result = total_cost
    return result

print(solution())