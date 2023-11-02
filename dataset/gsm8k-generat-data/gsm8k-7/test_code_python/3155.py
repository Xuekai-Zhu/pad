def solution():
    num_bars = 200
    num_friends = 4
    fraction_taken = 1/4
    num_bars_taken = num_bars * fraction_taken
    num_bars_per_person = num_bars_taken / (num_friends + 1) # Thomas and his 4 friends
    num_bars_returned = 5
    num_bars_taken_by_piper = num_bars_taken - num_bars_returned
    num_bars_taken_total = num_bars_taken + num_bars_taken_by_piper
    num_bars_left = num_bars - num_bars_taken_total
    result = num_bars_left
    return result

print(solution())