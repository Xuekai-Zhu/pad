def solution():
    # Calculate the total amount of flour needed
    total_flour = 12 * 4  # 4 pounds of flour per loaf, 12 loaves in total

    # Calculate the cost of buying a 10-pound bag of flour and a 12-pound bag of flour
    cost_10_pounds = 10
    cost_12_pounds = 13

    # Determine how many bags of each he needs to buy
    num_bags_10_pounds = total_flour // 10
    num_bags_12_pounds = total_flour // 12 + 1

    # Calculate the total cost of buying the flour
    total_cost = min(num_bags_10_pounds * cost_10_pounds, num_bags_12_pounds * cost_12_pounds)
    result = total_cost
    return result

print(solution())