def solution():
    """James writes a 3-page letter to 2 different friends twice a week. How many pages does he write a year?"""
    pages_per_letter = 3
    letters_per_week = 2
    weeks_per_year = 52
    total_pages = pages_per_letter * letters_per_week * weeks_per_year
    result = total_pages
    return result

print(solution())