def solution():
    """A farmer has 51 cows. The farmer adds five new cows to its herd and then sells a quarter of the herd. How many cows does the farmer have left?"""
    initial_cows = 51
    new_cows = 5
    total_cows = initial_cows + new_cows
    cows_sold = total_cows // 4
    remaining_cows = total_cows - cows_sold
    result = remaining_cows
    return result

print(solution())