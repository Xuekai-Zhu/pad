def solution():
    """Monica and Sheila are twins. Their mother gave them $50 and told them to buy some toilet paper and spend the remainder on groceries. The toilet paper cost $12. They bought apples, butter, eggs, and a large ham for twice the cost of the toilet paper. Since they still had some leftover money, they called their mother and she gave them permission to buy whatever they wanted for themselves as long as they shared the money evenly. They saw some boots they really liked, but a pair of boots costs 3 times the amount they had left. How much more would Monica and Sheila each have to add of their own money to buy two pairs of boots?"""
    initial_money = 50
    toilet_paper_cost = 12
    groceries_cost = 2 * toilet_paper_cost
    remaining_money = initial_money - toilet_paper_cost - groceries_cost
    cost_of_two_pairs_of_boots = 3 * remaining_money
    additional_money_needed = cost_of_two_pairs_of_boots - remaining_money
    money_each_needs_to_add = additional_money_needed / 2
    result = money_each_needs_to_add
    return result

print(solution())