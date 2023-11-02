def solution():
    # Calculate John's former monthly rent
    former_rent = 2 * 750

    # Calculate the amount John and his roommate split for their new apartment
    new_rent = 2800 / 2

    # Calculate the amount John saves per month
    savings_per_month = former_rent - new_rent

    # Calculate the amount John saves per year
    savings_per_year = savings_per_month * 12

    result = savings_per_year
    return result

print(solution())