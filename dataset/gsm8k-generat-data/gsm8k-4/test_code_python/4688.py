def solution():
    """Emily bought a shirt and a coat for $600. What does the shirt cost if it is one-third the price of the coat?"""
    # Define the price of the coat
    coat_price = None

    # Define the price of the shirt as one-third the price of the coat
    shirt_price = coat_price / 3

    # Define the total amount spent by Emily
    total_spent = 600

    # Use the equation total_spent = coat_price + shirt_price to solve for coat_price
    coat_price = (total_spent - shirt_price) / 2

    result = shirt_price
    return result

print(solution())