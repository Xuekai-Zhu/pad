def solution():
    daily_average = 40  # Krystian borrows an average of 40 books every day
    friday_increase = 0.4  # Krystian borrows 40% more books on Fridays
    friday_borrowed = daily_average * (1 + friday_increase)  # Krystian borrows this amount on a Friday

    # Calculate the total number of books Krystian borrows in a week
    total_borrowed = (daily_average * 4) + friday_borrowed  # The library is open from Monday to Friday

    result = total_borrowed
    return result

print(solution())