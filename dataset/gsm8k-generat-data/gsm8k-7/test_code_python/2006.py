def solution():
    starting_fee = 80
    yearly_increase = 10
    year = 6

    # Calculate the total increase from the starting fee
    total_increase = (year - 1) * yearly_increase

    # Calculate the membership fee in the given year
    membership_fee = starting_fee + total_increase
    result = membership_fee
    return result

print(solution())