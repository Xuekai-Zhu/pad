def solution():
    # Define the prices for each tier of knife sharpening
    first_knife_price = 5.00
    second_tier_price = 4.00
    third_tier_price = 3.00

    # Determine how many knives are in each tier
    second_tier_count = min(3, 9-1)
    third_tier_count = max(0, 9-4)

    # Calculate the total cost of sharpening all knives
    total_cost = (first_knife_price + second_tier_price*second_tier_count +
                  third_tier_price*third_tier_count)

    result = total_cost
    return result

print(solution())