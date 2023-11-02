def solution():
    # Calculate Olivia's new insurance premium after one accident and three tickets
    accident_increase = 0.1  # insurance premium increases by 10% for every accident
    ticket_increase = 5  # insurance premium increases by $5/month for every ticket
    new_premium = 50 * (1 + accident_increase) + 3 * ticket_increase
    result = new_premium
    return result

print(solution())