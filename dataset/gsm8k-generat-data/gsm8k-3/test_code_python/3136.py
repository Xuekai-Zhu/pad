def solution():
    """Mark wants to have a water balloon fight with his friends. He goes to the store to buy balloons and sees that they sell small bags for $4, medium bags for $6 and extra large bags for $12. He has $24 and wants to get the most balloons as possible. If the $4 bags contain 50 balloons, the $6 bags contain 75 balloons and the $12 bags contain 200 balloons, what is the greatest number of balloons he can buy?"""
    # Define the prices and number of balloons in each bag
    SMALL_PRICE = 4
    SMALL_BALLOONS = 50
    MEDIUM_PRICE = 6
    MEDIUM_BALLOONS = 75
    LARGE_PRICE = 12
    LARGE_BALLOONS = 200

    # Define Mark's budget
    budget = 24

    # Calculate the maximum number of each type of bag Mark can buy
    small_bags = budget // SMALL_PRICE
    medium_bags = budget // MEDIUM_PRICE
    large_bags = budget // LARGE_PRICE

    # Calculate the maximum number of balloons Mark can buy
    max_balloons = 0
    for sb in range(small_bags + 1):
        for mb in range(medium_bags + 1):
            for lb in range(large_bags + 1):
                total_price = sb * SMALL_PRICE + mb * MEDIUM_PRICE + lb * LARGE_PRICE
                if total_price <= budget:
                    total_balloons = sb * SMALL_BALLOONS + mb * MEDIUM_BALLOONS + lb * LARGE_BALLOONS
                    if total_balloons > max_balloons:
                        max_balloons = total_balloons

    # Display the maximum number of balloons Mark can buy
    result = max_balloons
    return result

print(solution())