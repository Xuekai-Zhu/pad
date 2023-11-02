def solution():
    """Hazel put up a lemonade stand. She sold half her lemonade to a construction crew. She sold 18 cups to kids on bikes. She gave away half that amount to her friends. Then she drank the last cup of lemonade herself. How many cups of lemonade did Hazel make?"""
    cups_sold_to_constructors = 0.5
    total_cups_sold_to_kids = 18
    cups_given_away = total_cups_sold_to_kids * 0.5
    cups_drunk = 1
    cups_made = (cups_sold_to_constructors + total_cups_sold_to_kids + cups_given_away + cups_drunk) * 2
    result = cups_made
    return result

print(solution())