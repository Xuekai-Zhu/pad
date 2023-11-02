def solution():
    # Calculate the total cost of items bought
    total_cost = (5 * 5) + (10 * 5) + (3 * 5)  # 5 packs of crayons at $5 each, 10 books at $5 each, and 3 calculators at $5 each

    # Calculate the change after buying items
    change = 200 - total_cost

    # Calculate how many bags Bruce can buy with the change
    bags = change // 10

    result = bags
    return result

print(solution())