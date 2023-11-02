def solution():
    total_bars = 200
    bars_taken = total_bars / 4
   bars_returned = 5
    bars_taken_by_sister = 5
    total_bars_left = total_bars - (bars_taken + bars_returned + bars_taken_by_sister)
    result = total_bars_left
    return result

print(solution())