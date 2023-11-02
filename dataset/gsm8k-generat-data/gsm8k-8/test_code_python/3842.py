def solution():
    # Define the variables
    shirt_to_pants_ratio = 3/4
    shoe_to_pants_difference = 10
    total_cost = 340

    # Calculate the price of the shirt and shoes
    shirt_price = shirt_to_pants_ratio * pants_price
    shoe_price = pants_price + shoe_to_pants_difference

    # Calculate the price of the pants
    pants_price = (total_cost - shirt_price - shoe_price) / 3
    result = pants_price
    return result

print(solution())