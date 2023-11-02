def solution():
    total_bars = 12  # The box contains 12 bars
    num_people = 3  # The bars are being shared equally among 3 people

    # Calculate the number of bars each person gets
    bars_per_person = total_bars / num_people

    # Calculate the number of bars Mike and Rita get combined
    combined_bars = bars_per_person * 2
    result = combined_bars
    return result

print(solution())