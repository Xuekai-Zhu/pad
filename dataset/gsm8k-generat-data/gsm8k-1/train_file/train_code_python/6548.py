def solution():
    """Benny has bought a new piggy bank and wants to start saving money. In January he adds $19, then adds the same amount in February. By the end of March, he has $46. How many dollars did he add to the piggy bank in March?"""
    january_amount = 19
    february_amount = january_amount
    march_amount = 46 - january_amount - february_amount
    result = march_amount
    return result

print(solution())