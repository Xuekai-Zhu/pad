def solution():
    """Reuben opens a sandwich shop selling his namesake sandwich and pastrami sandwiches. Pastrami cost $2 more than the Reuben. He sells 10 Reubens and 5 Pastrami sandwiches and earns $55. How much does a pastrami sandwich cost?"""
    num_reubens = 10
    num_pastrami = 5
    total_sandwiches = num_reubens + num_pastrami
    total_money_earned = 55
    difference_in_cost = 2
    cost_of_reuben = (total_money_earned - (num_pastrami * (cost_of_reuben + difference_in_cost))) / num_reubens
    cost_of_pastrami = cost_of_reuben + difference_in_cost
    result = cost_of_pastrami
    return result

print(solution())