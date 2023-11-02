def solution():
    """Mike buys 6 rose bushes at 75 dollars each, 2 of them are for his friend and the rest are for him. He also buys 2 tiger tooth aloes for 100 dollars each. How much money did he spend on plants for himself?"""
    # Calculate the total cost of the rose bushes
    rose_bushes = 6
    rose_bushes_cost = 75
    total_cost = rose_bushes * rose_bushes_cost

    # Calculate the cost of the rose bushes for his friend
    friend_cost = rose_bushes_cost * 2

    # Calculate the cost of the tiger tooth aloes
    aloes_cost = 100 * 2

    # Calculate the cost of the plants for himself
    self_cost = total_cost - friend_cost - aloes_cost
    
    result = self_cost
    return result

print(solution())