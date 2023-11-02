def solution():
    """Nancy is crafting clay pots to sell. She creates 12 clay pots on Monday, twice as many on Tuesday, a few more on Wednesday, then ends the week with 50 clay pots. How many did she create on Wednesday?"""
    monday_pots = 12
    tuesday_pots = monday_pots * 2
    total_pots = monday_pots + tuesday_pots + wednesday_pots + friday_pots
    wednesday_pots = total_pots - 50
    result = wednesday_pots
    return result

print(solution())