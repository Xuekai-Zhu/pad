def solution():
    """During a day at the farm, Annie picked eight pints of blueberries. Kathryn picked two pints more than Annie, and Ben picked three pints fewer than Kathryn. How many pints, in total, did the three pick together?"""
    annie_picked = 8
    kathryn_picked = annie_picked + 2
    ben_picked = kathryn_picked - 3
    total_picked = annie_picked + kathryn_picked + ben_picked
    result = total_picked
    return result

print(solution())