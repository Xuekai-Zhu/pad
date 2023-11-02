def solution():
    """Jake has $5000. He spends $2800 on a new motorcycle, and then spends half of what's left on a concert ticket. Jake then loses a fourth of what he has left. How much money does he have left?"""
    initial_money = 5000
    motorcycle_cost = 2800
    concert_cost = (initial_money - motorcycle_cost) / 2
    final_money = concert_cost - (concert_cost / 4)
    result = final_money
    return result

print(solution())