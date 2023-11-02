def solution():
    """Luca went to a sandwich shop for lunch. The sandwich he bought was normally $8, but he had a coupon for a quarter of the price off. He then upgraded it with sliced avocado for an extra dollar. After adding a drink and a $3 salad, his total lunch bill was $12. How many dollars did Luca pay for his drink?"""
    # Define the price of the sandwich and the discount percentage
    sandwich_price = 8
    discount_percent = 0.25

    # Calculate the discount amount and the new price of the sandwich
    discount_amount = sandwich_price * discount_percent
    new_sandwich_price = sandwich_price - discount_amount

    # Add the price of the sliced avocado to the sandwich price
    upgraded_sandwich_price = new_sandwich_price + 1

    # Calculate the total bill before adding the drink price
    total_before_drink = upgraded_sandwich_price + 3

    # Calculate the price of the drink by subtracting the total bill from the actual amount paid
    drink_price = 12 - total_before_drink

    result = drink_price
    return result

print(solution())