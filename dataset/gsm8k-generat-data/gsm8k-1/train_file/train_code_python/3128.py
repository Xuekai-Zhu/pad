def solution():
    """Mike buys 6 rose bushes at 75 dollars each, 2 of them are for his friend and the rest are for him. He also buys 2 tiger tooth aloes for 100 dollars each. How much money did he spend on plants for himself?"""
    num_rose_bushes = 6
    cost_per_rose_bush = 75
    num_rose_bushes_for_friend = 2
    num_rose_bushes_for_self = num_rose_bushes - num_rose_bushes_for_friend
    cost_of_rose_bushes_for_self = num_rose_bushes_for_self * cost_per_rose_bush
    num_tiger_tooth_aloes = 2
    cost_per_tiger_tooth_aloe = 100
    total_cost = cost_of_rose_bushes_for_self + (num_tiger_tooth_aloes * cost_per_tiger_tooth_aloe)
    result = total_cost
    return result

print(solution())