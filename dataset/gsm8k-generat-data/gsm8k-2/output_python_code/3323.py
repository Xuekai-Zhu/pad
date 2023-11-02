def solution():
    """Monica and Sheila are twins. Their mother gave them $50 and told them to buy some toilet paper and spend the remainder on groceries. The toilet paper cost $12. They bought apples, butter, eggs, and a large ham for twice the cost of the toilet paper. Since they still had some leftover money, they called their mother and she gave them permission to buy whatever they wanted for themselves as long as they shared the money evenly. They saw some boots they really liked, but a pair of boots costs 3 times the amount they had left. How much more would Monica and Sheila each have to add of their own money to buy two pairs of boots?"""
    total_money = 50
    toilet_paper_cost = 12
    groceries_cost = 2 * toilet_paper_cost
    remaining_money = total_money - toilet_paper_cost - groceries_cost
    boots_cost = 3 * remaining_money
    total_boots_cost = 2 * boots_cost
    each_share = (remaining_money - boots_cost) / 2
    money_needed = each_share - boots_cost
    result = money_needed
    return result

print(solution())