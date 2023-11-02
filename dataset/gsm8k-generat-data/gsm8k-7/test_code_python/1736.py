def solution():
    num_people = 3
    total_bars = 12

    # Calculate the number of bars each person gets
    bars_per_person = total_bars / num_people

    # Calculate the total number of bars that Mike and Rita get
    mike_and_rita_bars = bars_per_person * 2

    result = mike_and_rita_bars
    return result

print(solution())