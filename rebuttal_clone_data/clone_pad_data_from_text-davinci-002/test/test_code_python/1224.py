def solution():
    initial_amount = 10000
    friends_donation = initial_amount * 0.40
    family_donation = (initial_amount - friends_donation) * 0.30
    total_donation = friends_donation + family_donation
    personal_savings = initial_amount - total_donation
    result = personal_savings
    return result

print(solution())