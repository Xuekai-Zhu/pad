def solution():
    """Martha needs 4 cups of berries and 2 cups of heavy cream to make 1 quart of ice cream. She wants to make 1 quart of strawberry ice cream and 1 quart of raspberry ice cream. At the farmers market, the 2 cup packages of strawberries are $3.00 each and the 2 cup package of raspberries are $5.00 each. The heavy cream is sold for $4.00 for a 4 cup container. How much will it cost her to make 1 quart of each ice cream?"""
    strawberries_needed = 4
    raspberries_needed = 4
    heavy_cream_needed = 2

    strawberries_cost = 3 * 2  # 2 cups of strawberries needed
    raspberries_cost = 5 * 2  # 2 cups of raspberries needed
    heavy_cream_cost = 4

    total_cost = (strawberries_cost + raspberries_cost + heavy_cream_cost) * 2
    result = total_cost
    return result

print(solution())