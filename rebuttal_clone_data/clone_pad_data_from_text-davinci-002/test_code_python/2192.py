def solution():
    kilometers = 5
    initial_donation = 10
    subsequent_donation = initial_donation * 2
    total_donation = initial_donation + (subsequent_donation * (kilometers - 1))
    result = total_donation
    return result

print(solution())