def solution():
    """Kimberly went strawberry picking with her family over the weekend. She picked 8 times the amount of strawberries her brother picked and her parents picked 93 strawberries less than her. If her brother picked 3 baskets each containing 15 strawberries, how many strawberries would they each have if they divide the total number of strawberries equally amongst them?"""
    brother_picked = 3 * 15
    kimberly_picked = 8 * brother_picked
    parents_picked = kimberly_picked - 93
    total_picked = brother_picked + kimberly_picked + parents_picked
    strawberries_per_person = total_picked / 4
    result = strawberries_per_person
    return result

print(solution())