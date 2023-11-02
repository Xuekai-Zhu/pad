def solution():
    """Luca went to a sandwich shop for lunch. The sandwich he bought was normally $8, but he had a coupon for a quarter of the price off. He then upgraded it with sliced avocado for an extra dollar. After adding a drink and a $3 salad, his total lunch bill was $12. How many dollars did Luca pay for his drink?"""
    # Define the price of the sandwich and the discount Luca received
    SANDWICH_PRICE = 8
    DISCOUNT = 0.25

    # Calculate the price of the sandwich after the discount
    sandwich_price = SANDWICH_PRICE * (1 - DISCOUNT)

    # Add the cost of sliced avocado to the sandwich price
    sandwich_price += 1

    # Add the cost of a drink and salad to the sandwich price
    total_bill = sandwich_price + 3

    # Calculate the cost of the drink
    drink_price = total_bill - sandwich_price

    # Display the cost of the drink
    result = drink_price
    return result

print(solution())