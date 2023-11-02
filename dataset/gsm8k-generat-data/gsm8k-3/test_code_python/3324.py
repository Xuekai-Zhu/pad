def solution():
    """Monica and Sheila are twins. Their mother gave them $50 and told them to buy some toilet paper and spend the remainder on groceries. The toilet paper cost $12. They bought apples, butter, eggs, and a large ham for twice the cost of the toilet paper. Since they still had some leftover money, they called their mother and she gave them permission to buy whatever they wanted for themselves as long as they shared the money evenly. They saw some boots they really liked, but a pair of boots costs 3 times the amount they had left. How much more would Monica and Sheila each have to add of their own money to buy two pairs of boots?"""
    # Define the cost of the toilet paper and the multiplier for the groceries
    TP_COST = 12
    GROCERIES_MULT = 2

    # Calculate the cost of the groceries and the total spent
    groceries_cost = GROCERIES_MULT * TP_COST
    total_spent = TP_COST + groceries_cost

    # Calculate the leftover money and the amount each twin can spend on themselves
    leftover_money = 50 - total_spent
    individual_money = leftover_money / 2

    # Calculate the cost of two pairs of boots and the amount each twin needs to add
    boots_cost = 3 * individual_money
    amount_needed = boots_cost - individual_money

    # Display the amount each twin needs to add
    result = amount_needed
    return result

print(solution())