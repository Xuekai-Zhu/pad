def solution():
    """Kim has started his own housekeeping business and is calculating how much profit he will make from his clients. He already has 3 clients, but is talking to another 5 potential clients and feels confident enough to include them in his calculations. Each client’s home will need 2 bottles of bleach and a pack of cloths to clean. Bottles of bleach will cost $2 each and packs of cloths will cost $5 each. These are his only expenses. He calculates that his total income each week will be $92. Profit is the difference between total income and total expenses, so how much profit, in dollars, will Lucas make each week?"""
    num_existing_clients = 3
    num_potential_clients = 5
    total_clients = num_existing_clients + num_potential_clients
    bleach_cost = 2
    cloths_cost = 5
    total_expenses = total_clients * (2 * bleach_cost + cloths_cost)
    total_income = 92
    profit = total_income - total_expenses
    result = profit
    
    return result

print(solution())