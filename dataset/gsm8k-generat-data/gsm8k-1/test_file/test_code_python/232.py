def solution():
    """Ram uses a lot of pens. He discovered that he can save money by mixing the ink from five empty pens to make one full pen. If he buys 25 pens and then uses them to make new pens when the ink runs low, how many total pens does he get to have?"""
    starting_pens = 25
    pens_to_make_one = 5
    empty_pens_needed = pens_to_make_one - 1
    total_pens = starting_pens + (starting_pens * empty_pens_needed)
    result = total_pens
    return result

print(solution())