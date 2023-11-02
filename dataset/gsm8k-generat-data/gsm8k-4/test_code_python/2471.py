def solution():
    """John books 3 nights at a hotel room for $250 a night. He has a $100 discount. How much does he pay?"""
    # Define the number of nights and the price per night
    nights = 3
    price_per_night = 250

    # Define the discount amount
    discount = 100

    # Calculate the total cost without the discount
    total_cost = nights * price_per_night

    # Subtract the discount from the total cost
    final_cost = total_cost - discount

    result = final_cost
    return result

print(solution())