def solution():
    initial_fee = 80  # Aaron pays $80 in the first year
    yearly_increase = 10  # The membership fee increases by $10 each year
    years = 6  # We want to calculate the membership fee in the sixth year

    # Calculate the membership fee in the sixth year
    membership_fee = initial_fee + (years - 1) * yearly_increase
    result = membership_fee
    return result

print(solution())