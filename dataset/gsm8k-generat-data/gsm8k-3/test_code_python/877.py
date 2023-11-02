def solution():
    """Kimberly went strawberry picking with her family over the weekend. She picked 8 times the amount of strawberries her brother picked and her parents picked 93 strawberries less than her. If her brother picked 3 baskets each containing 15 strawberries, how many strawberries would they each have if they divide the total number of strawberries equally amongst them?"""
    # Define the number of strawberries her brother picked
    brother_strawberries = 3 * 15

    # Calculate the number of strawberries Kimberly picked
    kimberly_strawberries = 8 * brother_strawberries

    # Calculate the number of strawberries her parents picked
    parents_strawberries = kimberly_strawberries - 93

    # Calculate the total number of strawberries
    total_strawberries = brother_strawberries + kimberly_strawberries + parents_strawberries

    # Calculate the number of strawberries each person would have if divided equally
    strawberries_per_person = total_strawberries / 4

    # Display the number of strawberries per person
    result = strawberries_per_person
    return result

print(solution())