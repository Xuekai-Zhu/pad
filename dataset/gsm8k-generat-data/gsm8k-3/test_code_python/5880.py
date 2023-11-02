def solution():
    """Nedy can eat 8 packs of crackers from Monday to Thursday. If Nedy ate twice the amount on Friday, how many crackers did Nedy eat in all?"""
    # Define the number of packs of crackers Nedy eats each day from Monday to Thursday
    daily_crackers = 8 / 4

    # Calculate the number of packs of crackers Nedy eats on Friday
    friday_crackers = daily_crackers * 2

    # Calculate the total number of packs of crackers Nedy eats in one week
    total_crackers = daily_crackers * 4 + friday_crackers

    # Display the total number of packs of crackers Nedy ate
    result = total_crackers
    return result

print(solution())