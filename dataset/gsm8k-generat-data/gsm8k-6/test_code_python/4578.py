def solution():
    # Calculate how many payments Grace will receive to make 1800 dollars
    num_payments = 1800 / 300  # Grace charges 300 dollars per week
    weeks = num_payments * 2  # her client pays every 2 weeks
    result = weeks
    return result

print(solution())