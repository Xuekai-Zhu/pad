def solution():
    """Colston knows that his teacher loves drinking coffee and one day wants to see how much she drinks each week. He sees that she has a 20-ounce thermos and when she makes her coffee she pours a 1/2 cup of milk in, and then fills the coffee to the top. She does this twice a day. After the five-day school week, she decides to drink 1/4 of what she normally drinks. How many ounces of coffee does she now drink a week?"""
    thermos_size = 20
    milk_per_cup = 0.5
    coffee_per_cup = thermos_size - milk_per_cup
    cups_per_day = 2
    days_per_week = 5
    total_coffee = coffee_per_cup * cups_per_day * days_per_week
    reduced_amount = total_coffee * 0.25
    result = reduced_amount
    return result

print(solution())