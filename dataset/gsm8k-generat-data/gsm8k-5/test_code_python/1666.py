def solution():
    price_per_pack = 0.5  # Calvin buys a pack of chips for $0.50
    packs_per_week = 5  # Calvin buys 5 packs of chips per week
    weeks = 4  # Calvin wants to know how much money he has spent on chips after 4 weeks

    # Calculate the total amount of money Calvin has spent on chips
    total_spent = price_per_pack * packs_per_week * weeks
    result = total_spent
    return result

print(solution())