def solution():
    # Define the number of chocolate bars in the box
    total_bars = 12

    # Calculate how many bars each person gets
    bars_per_person = total_bars / 3

    # Calculate how many bars Mike and Rita get combined
    mike_and_rita_bars = bars_per_person * 2

    result = mike_and_rita_bars
    return result

print(solution())