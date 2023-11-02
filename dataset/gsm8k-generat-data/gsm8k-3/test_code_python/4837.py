def solution():
    """Fern buys one pair of high heels for $60 and five pairs of ballet slippers for 2/3rds of the price of the high heels. How much does she pay total?"""
    # Define the price of the high heels
    high_heels_price = 60

    # Calculate the price of one pair of ballet slippers
    ballet_slippers_price = (2/3) * high_heels_price

    # Calculate the total cost of five pairs of ballet slippers
    total_ballet_slippers_cost = 5 * ballet_slippers_price

    # Calculate the total cost of Fern's purchase
    total_cost = high_heels_price + total_ballet_slippers_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())