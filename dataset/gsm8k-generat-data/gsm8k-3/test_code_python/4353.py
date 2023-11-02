def solution():
    """Norris saved $29 in September. He saved $25 in October and $31 in November. Then Hugo spent $75 on an online game. How much money does Norris have left?"""
    # Calculate how much Norris saved
    total_saved = 29 + 25 + 31

    # Calculate how much money Norris has left after Hugo spent $75
    remaining_money = total_saved - 75

    # Display how much money Norris has left
    result = remaining_money
    return result

print(solution())