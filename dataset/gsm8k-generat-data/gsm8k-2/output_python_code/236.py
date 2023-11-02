def solution():
    """Jake has $5000. He spends $2800 on a new motorcycle, and then spends half of what's left on a concert ticket. Jake then loses a fourth of what he has left. How much money does he have left?"""
    starting_amount = 5000
    motorcycle_cost = 2800
    concert_cost = (starting_amount - motorcycle_cost) / 2
    remaining_amount = starting_amount - motorcycle_cost - concert_cost
    lost_amount = remaining_amount / 4
    final_amount = remaining_amount - lost_amount
    result = final_amount
    return result

print(solution())