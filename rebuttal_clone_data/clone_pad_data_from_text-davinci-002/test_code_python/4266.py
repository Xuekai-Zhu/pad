def solution():
    total_chocolate_bars = 20
    chocolate_bars_shared = total_chocolate_bars / 5
    chocolate_bars_given_up = chocolate_bars_shared / 2
    chocolate_bars_received = chocolate_bars_given_up * 3
    chocolate_bars_eaten = chocolate_bars_given_up * 2
    chocolate_bars_left = chocolate_bars_received - chocolate_bars_eaten
    result = chocolate_bars_left
    return result

print(solution())