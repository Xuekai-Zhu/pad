def solution():
    """Colston knows that his teacher loves drinking coffee and one day wants to see how much she drinks each week. He sees that she has a 20-ounce thermos and when she makes her coffee she pours a 1/2 cup of milk in, and then fills the coffee to the top. She does this twice a day. After the five-day school week, he decides to tell her, and when she hears how much coffee she drinks, she decides to drink 1/4 of what she normally drinks. How many ounces of coffee does she now drink a week?"""
    thermos_size = 20
    milk_cup_size = 0.5
    coffee_size = thermos_size - milk_cup_size
    cups_per_day = 2
    days_per_week = 5
    total_coffee_per_week = coffee_size * cups_per_day * days_per_week
    reduced_coffee_per_week = total_coffee_per_week * 0.25
    result = reduced_coffee_per_week
    return result

print(solution())