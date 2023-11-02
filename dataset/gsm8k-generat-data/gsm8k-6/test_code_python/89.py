def solution():
    # Calculate the total number of books borrowed by Krystian in a week
    daily_average = 40
    friday_increase = daily_average * 0.4
    friday_total = daily_average + friday_increase
    total_books = (daily_average * 4) + friday_total  # library is open from Monday to Friday
    result = total_books
    return result

print(solution())