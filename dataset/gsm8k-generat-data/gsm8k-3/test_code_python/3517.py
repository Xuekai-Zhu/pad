def solution():
    """Hayden eats 1 oz of mixed nuts as an evening snack. He buys the bulk bag of mixed nuts that cost $25.00 a bag and holds 40 oz of mixed nuts. There is currently a $5.00 coupon for this item. How much will each serving of nuts cost, in cents, after the coupon is applied?"""

    # Define the cost of the bag of mixed nuts and the amount of nuts it contains
    bag_cost = 25.00
    bag_size = 40

    # Define the cost of each ounce of nuts before the coupon is applied
    cost_per_ounce = bag_cost / bag_size

    # Define the value of the coupon
    coupon_value = 5.00

    # Calculate the new cost of the bag after the coupon is applied
    new_cost = bag_cost - coupon_value

    # Calculate the new cost per ounce of nuts
    new_cost_per_ounce = new_cost / bag_size

    # Convert the new cost per ounce to cents
    cost_per_serving = new_cost_per_ounce * 100

    # Display the cost per serving in cents
    result = cost_per_serving
    return result

print(solution())