def solution():
    # Calculate the total amount spent on clothes
    total_spent = 2 * 18.5 + 63  # cost of 2 shirts and 1 pair of trousers
    remaining_budget = 260 - total_spent  # amount of money remaining
    num_items = 4  # number of items purchased with remaining budget
    cost_per_item = remaining_budget / num_items  # cost of each item if split evenly
    result = cost_per_item
    return result

print(solution())