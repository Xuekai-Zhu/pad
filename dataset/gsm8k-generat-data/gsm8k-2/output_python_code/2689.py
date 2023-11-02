def solution():
    """Bonnie and Samuel went to the market together. Bonnie bought 8 apples. Samuel bought 20 more apples than Bonnie. Samuel then ate half of them and used 1/7 of them to make apple pie. How many apples does Samuel have left?"""
    bonnie_apples = 8
    samuel_apples = bonnie_apples + 20
    samuel_apples = samuel_apples / 2   # Samuel ate half of the apples
    samuel_apples = samuel_apples - (samuel_apples / 7)   # Samuel used 1/7 of the apples to make pie
    result = samuel_apples
    return result

print(solution())