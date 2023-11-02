def solution():
    """Annika brought $50 to the town fair. She spent half of it on food and snacks, and an additional $10 for rides. How much, in dollars, is left?"""
    initial_money = 50
    food_spending = initial_money / 2
    ride_spending = 10
    remaining_money = initial_money - food_spending - ride_spending
    result = remaining_money
    return result

print(solution())