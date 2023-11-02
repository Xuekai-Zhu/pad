def solution():
    """Monica and Sheila are twins. Their mother gave them $50 and told them to buy some toilet paper and spend the remainder on groceries. The toilet paper cost $12. They bought apples, butter, eggs, and a large ham for twice the cost of the toilet paper. Since they still had some leftover money, they called their mother and she gave them permission to buy whatever they wanted for themselves as long as they shared the money evenly. They saw some boots they really liked, but a pair of boots costs 3 times the amount they had left. How much more would Monica and Sheila each have to add of their own money to buy two pairs of boots?"""
    # Define the initial amount of money given by their mother
    initial_money = 50
    
    # Define the cost of the toilet paper
    toilet_paper_cost = 12
    
    # Calculate the cost of the groceries they bought
    groceries_cost = 2 * toilet_paper_cost
    
    # Calculate the total amount of money spent
    total_spent = toilet_paper_cost + groceries_cost
    
    # Calculate the amount of money left after buying the toilet paper and groceries
    money_left = initial_money - total_spent
    
    # Calculate the cost of one pair of boots
    boots_cost = 3 * money_left
    
    # Calculate the total cost of two pairs of boots
    total_boots_cost = 2 * boots_cost
    
    # Calculate the amount each twin has to contribute to buy two pairs of boots
    contribution = total_boots_cost / 2
    
    # Calculate how much more each twin has to contribute
    extra_contribution = contribution - money_left
    
    result = extra_contribution
    return result

print(solution())