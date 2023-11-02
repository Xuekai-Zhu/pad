def solution():
    # Calculate how many books Evan owns now
    Evan_own_now = 200 - 2 - 40

    # Calculate how many books Evan will have in 5 years
    Evan_in_5_years = 5 * (Evan_own_now * 5 + 60)

    # Calculate the total number of books Evan will have in 5 years
    total_books = Evan_own_now + Evan_in_5_years
    
    result = total_books
    return result

print(solution())