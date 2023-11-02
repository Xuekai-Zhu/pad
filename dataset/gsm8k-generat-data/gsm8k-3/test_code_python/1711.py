def solution():
    """A waterpark opens up and charges $30 for admission.  Kids' tickets are half price.  If a group of people brings a soda, they can get 20% off the total price of admission.  Janet gets tickets for 10 people and 4 of them are children.  She buys a soda for $5 to take advantage of the discount for her group.  How much did she pay for everything?"""
    # Define the regular admission price and the discount percentage
    REGULAR_PRICE = 30
    DISCOUNT_PERCENTAGE = 0.2

    # Calculate the total number of adult and child tickets
    num_adults = 10 - 4
    num_children = 4

    # Calculate the total cost of the adult tickets and the child tickets
    adult_cost = num_adults * REGULAR_PRICE
    child_cost = num_children * (REGULAR_PRICE / 2)

    # Calculate the total cost before the discount
    total_cost = adult_cost + child_cost

    # Apply the discount if a soda was purchased
    soda_price = 5
    if soda_price:
        total_cost = total_cost * (1 - DISCOUNT_PERCENTAGE)

    # Display the total cost
    result = total_cost
    return result

print(solution())