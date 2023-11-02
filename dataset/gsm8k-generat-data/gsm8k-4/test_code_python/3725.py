def solution():
    """At Peanut Emporium, peanuts cost $3 per pound with a 15-pound minimum. If Baxter spent $105 on peanuts, how many pounds over the minimum did he purchase?"""
    # Define the price per pound and the minimum purchase
    price_per_pound = 3
    minimum_purchase = 15

    # Calculate the total number of pounds of peanuts purchased
    total_pounds = int(105 / price_per_pound)

    # Calculate the number of pounds over the minimum purchase
    over_minimum = total_pounds - minimum_purchase

    # Check if the purchase meets the minimum requirement
    if total_pounds >= minimum_purchase:
        result = over_minimum
    else:
        result = "Not enough peanuts purchased"
    return result

print(solution())