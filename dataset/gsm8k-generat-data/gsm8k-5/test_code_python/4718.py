def solution():
    pages_per_hour = 5  # James can write 5 pages per hour
    hours_per_night = 3  # James writes from 1 PM to 4 PM every night, which is 3 hours
    pages_per_night = pages_per_hour * hours_per_night  # James can write this many pages every night
    total_pages = 735  # James's book has 735 pages

    # Calculate the number of nights required to finish the book
    nights_required = total_pages / pages_per_night
    weeks_required = nights_required / 7  # Assume one week has 7 days

    result = weeks_required
    return result

print(solution())