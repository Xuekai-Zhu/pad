def solution():
    """A box of chocolate bars was shared equally between Mike, Rita and Anita. If the box contains 12 bars, how many bars did Mike and Rita get (combined)?"""
    # Define the number of chocolate bars in the box
    total_bars = 12

    # Divide the bars equally among the three people
    bars_per_person = total_bars / 3

    # Calculate the number of bars Mike and Rita got combined
    combined_bars = bars_per_person * 2

    result = combined_bars
    return result

print(solution())