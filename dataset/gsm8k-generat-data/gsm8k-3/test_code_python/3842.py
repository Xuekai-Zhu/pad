def solution():
    """Mark bought a shirt, pants, and shoes for $340. What is the price of the pants knowing that the price of a shirt is three-quarters of the price of the pants and that the price of a shoe is ten dollars more than the price of the pants?"""
    # Define variables and equations based on the problem description
    shirt_price = 0.75 * pants_price
    shoe_price = pants_price + 10
    total_price = shirt_price + pants_price + shoe_price
    total_price = 340

    # Solve for the price of the pants
    pants_price = (total_price - shirt_price - shoe_price) / 2

    # Display the price of the pants
    result = pants_price
    return result

print(solution())