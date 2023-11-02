def solution():
    # Calculate how many bars Thomas and his friends took
    bars_taken = 200 * 1/4

    # Divide the bars equally between Thomas and his 4 friends
    bars_per_person = bars_taken / 5

    # One friend returns 5 bars
    bars_returned = 5
    bars_left = bars_taken - bars_returned

    # Piper takes 5 fewer bars than Thomas and his friends
    piper_bars = bars_taken - 5

    # Calculate the total number of bars left
    bars_left = 200 - bars_taken + bars_returned - piper_bars
    result = bars_left
    return result

print(solution())