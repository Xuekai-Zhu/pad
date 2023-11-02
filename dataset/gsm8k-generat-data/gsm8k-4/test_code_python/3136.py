def solution():
    """Mark wants to have a water balloon fight with his friends. He goes to the store to buy balloons and sees that they sell small bags for $4, medium bags for $6 and extra large bags for $12. He has $24 and wants to get the most balloons as possible. If the $4 bags contain 50 balloons, the $6 bags contain 75 balloons and the $12 bags contain 200 balloons, what is the greatest number of balloons he can buy?"""
    # Define the prices and number of balloons per bag
    small_price = 4
    small_balloons = 50
    medium_price = 6
    medium_balloons = 75
    large_price = 12
    large_balloons = 200

    # Define the total budget
    total_budget = 24

    # Calculate the maximum number of small bags that can be purchased
    max_small_bags = total_budget // small_price

    # Calculate the maximum number of medium bags that can be purchased
    max_medium_bags = total_budget // medium_price

    # Calculate the maximum number of large bags that can be purchased
    max_large_bags = total_budget // large_price

    # Initialize the maximum number of balloons
    max_balloons = 0

    # Loop through all possible combinations and find the maximum number of balloons
    for small in range(max_small_bags + 1):
        for medium in range(max_medium_bags + 1):
            for large in range(max_large_bags + 1):
                # Calculate the total cost and total number of balloons for this combination
                total_cost = small * small_price + medium * medium_price + large * large_price
                total_balloons = small * small_balloons + medium * medium_balloons + large * large_balloons
                # If the total cost is within the budget and the total balloons is greater than the current maximum, update the maximum
                if total_cost <= total_budget and total_balloons > max_balloons:
                    max_balloons = total_balloons

    # Return the maximum number of balloons
    result = max_balloons
    return result

print(solution())