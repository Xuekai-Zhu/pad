def solution():
    """Benny has bought a new piggy bank and wants to start saving money. In January he adds $19, then adds the same amount in February. By the end of March, he has $46. How many dollars did he add to the piggy bank in March?"""
    # Define the amount added in January
    january_addition = 19

    # Calculate the amount added in February
    february_addition = january_addition

    # Define the total amount by the end of March
    total_amount = 46

    # Calculate the amount added in March
    march_addition = total_amount - (january_addition + february_addition)

    # return the result
    result = march_addition
    return result

print(solution())