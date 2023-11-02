def solution():
    # Calculate the cost per ounce for each bottle of ketchup
    cost_per_oz_1 = 1/10
    cost_per_oz_2 = 2/16
    cost_per_oz_3 = 2.5/25
    cost_per_oz_4 = 5/50
    cost_per_oz_5 = 10/200

    # Determine the maximum number of ounces of ketchup that can be purchased with $10
    max_oz = 10/cost_per_oz_1

    # Initialize variables to keep track of the number of bottles purchased and the remaining budget
    num_bottles = 0
    remaining_budget = 10

    # Check each bottle of ketchup to see if it can be purchased within the budget and, if so, purchase it
    if cost_per_oz_2 <= remaining_budget/max_oz:
        num_bottles += 1
        remaining_budget -= cost_per_oz_2 * 16
    if cost_per_oz_3 <= remaining_budget/max_oz:
        num_bottles += 1
        remaining_budget -= cost_per_oz_3 * 25
    if cost_per_oz_4 <= remaining_budget/max_oz:
        num_bottles += 1
        remaining_budget -= cost_per_oz_4 * 50
    if cost_per_oz_5 <= remaining_budget/max_oz:
        num_bottles += 1
        remaining_budget -= cost_per_oz_5 * 200

    # Determine the number of bottles of ketchup purchased
    num_bottles += int(remaining_budget/cost_per_oz_1)

    result = num_bottles
    return result

print(solution())