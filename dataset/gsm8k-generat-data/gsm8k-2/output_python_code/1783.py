def solution():
    """Nancy has a bag containing 22 tortilla chips. She gives 7 tortilla chips to her brother and 5 tortilla chips to her sister, keeping the rest for herself. How many did Nancy keep for herself?"""
    total_chips = 22
    brother_chips = 7
    sister_chips = 5
    nancy_chips = total_chips - brother_chips - sister_chips
    result = nancy_chips
    return result

print(solution())