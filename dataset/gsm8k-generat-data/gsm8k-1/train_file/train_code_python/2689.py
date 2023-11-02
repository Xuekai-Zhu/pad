def solution():
    """Bonnie and Samuel went to the market together. Bonnie bought 8 apples. Samuel bought 20 more apples than Bonnie. Samuel then ate half of them and used 1/7 of them to make apple pie. How many apples does Samuel have left?"""
    bonnie_apples = 8
    samuel_apples = bonnie_apples + 20
    samuel_apples_remaining = samuel_apples / 2 - samuel_apples / 7
    result = samuel_apples_remaining
    return result

print(solution())