def solution():
    """During a day at the farm, Annie picked eight pints of blueberries. Kathryn picked two pints more than Annie, and Ben picked three pints fewer than Kathryn. How many pints, in total, did the three pick together?"""
    annie_pints = 8
    kathryn_pints = annie_pints + 2
    ben_pints = kathryn_pints - 3
    total_pints = annie_pints + kathryn_pints + ben_pints
    result = total_pints
    return result

print(solution())