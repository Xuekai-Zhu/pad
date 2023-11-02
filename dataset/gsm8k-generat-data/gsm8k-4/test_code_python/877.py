def solution():
    """Kimberly went strawberry picking with her family over the weekend. She picked 8 times the amount of strawberries her brother picked and her parents picked 93 strawberries less than her. If her brother picked 3 baskets each containing 15 strawberries, how many strawberries would they each have if they divide the total number of strawberries equally amongst them?"""
    # Calculate the number of strawberries picked by Kimberly's brother
    brother_strawberries = 3 * 15

    # Calculate the number of strawberries picked by Kimberly
    kimberly_strawberries = 8 * brother_strawberries

    # Calculate the number of strawberries picked by Kimberly's parents
    parents_strawberries = kimberly_strawberries - 93

    # Calculate the total number of strawberries picked
    total_strawberries = brother_strawberries + kimberly_strawberries + parents_strawberries

    # Divide the total number of strawberries equally among the family members
    strawberries_per_person = total_strawberries // 4

    # return the result
    result = strawberries_per_person
    return result

print(solution())