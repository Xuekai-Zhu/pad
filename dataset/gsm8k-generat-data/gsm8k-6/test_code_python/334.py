def solution():
    # Calculate the cost of ingredients for 1 quart of each ice cream
    strawberry_cost = (4/2) * 3  # 4 cups of berries needed for 1 quart, and each package has 2 cups for $3.00
    raspberry_cost = (4/2) * 5  # 4 cups of berries needed for 1 quart, and each package has 2 cups for $5.00
    cream_cost = 4  # 2 cups of heavy cream needed for 1 quart, and a 4 cup container costs $4.00
    total_cost = strawberry_cost + raspberry_cost + cream_cost
    result = total_cost
    return result

print(solution())