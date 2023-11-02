def solution():
    """Elise has been selling her Dad's collection of 250 books for three years. Each book sells at 20$, and she sold twice as many books in the first year as she has sold in the current year. There are currently 50 unsold books, and her sales number this year is 45. What's the total amount of money she earned in the second year?"""
    total_books = 250
    current_year_sales = 45
    unsold_books = 50
    first_year_sales = 2 * current_year_sales
    second_year_sales = total_books - (current_year_sales + first_year_sales + unsold_books)
    earnings = second_year_sales * 20
    result = earnings
    return result

print(solution())