def solution():
    """Martha needs 4 cups of berries and 2 cups of heavy cream to make 1 quart of ice cream.  She wants to make 1 quart of strawberry ice cream and 1 quart of raspberry ice cream.  At the farmers market, the 2 cup packages of strawberries are $3.00 each and the 2 cup package of raspberries are $5.00 each.  The heavy cream is sold for $4.00 for a 4 cup container.  How much will it cost her to make 1 quart of each ice cream?"""
    # Define the amount and cost of the ingredients needed for 1 quart of each ice cream
    BERRIES_NEEDED = 4
    CREAM_NEEDED = 2
    STRAWBERRY_COST = 3
    RASPBERRY_COST = 5
    CREAM_COST = 4

    # Calculate the cost of the ingredients needed for 1 quart of strawberry ice cream
    strawberry_berries_cost = 2 * STRAWBERRY_COST
    strawberry_cream_cost = CREAM_COST / 2
    strawberry_total_cost = strawberry_berries_cost + strawberry_cream_cost

    # Calculate the cost of the ingredients needed for 1 quart of raspberry ice cream
    raspberry_berries_cost = 2 * RASPBERRY_COST
    raspberry_cream_cost = CREAM_COST / 2
    raspberry_total_cost = raspberry_berries_cost + raspberry_cream_cost

    # Calculate the total cost of making 1 quart of each ice cream
    total_cost = strawberry_total_cost + raspberry_total_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())