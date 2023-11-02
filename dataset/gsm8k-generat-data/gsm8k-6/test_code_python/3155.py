def solution():
    # Calculate the number of bars taken by Thomas and his friends
    bars_taken = 200 * (1/4)

    # Calculate the number of bars left after they divided them equally
    bars_left = bars_taken - (bars_taken % 5)

    # Subtract the bars returned by Thomas's friend
    bars_left -= 5

    # Calculate the number of bars taken by Piper
    bars_piper = bars_taken - 5

    # Calculate the total number of bars left in the box
    total_bars_left = 200 - bars_taken + bars_left + bars_piper

    result = total_bars_left
    return result

print(solution())