def solution():
    """A farmer has 51 cows. The farmer adds five new cows to its herd and then sells a quarter of the herd. How many cows does the farmer have left?"""
    initial_cows = 51
    new_cows = 5
    total_cows = initial_cows + new_cows
    sold_cows = total_cows * 0.25
    remaining_cows = total_cows - sold_cows
    result = remaining_cows
    return result

print(solution())