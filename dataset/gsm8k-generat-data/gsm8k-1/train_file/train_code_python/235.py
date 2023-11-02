def solution():
    """Jake has $5000. He spends $2800 on a new motorcycle, and then spends half of what's left on a concert ticket. Jake then loses a fourth of what he has left. How much money does he have left?"""
    starting_balance = 5000
    motorcycle_cost = 2800
    balance_after_motorcycle = starting_balance - motorcycle_cost
    balance_after_concert = balance_after_motorcycle / 2
    balance_after_loss = balance_after_concert * 0.75
    result = balance_after_loss
    return result

print(solution())