def solution():
    eggs_per_week = 10 + 14 + (14/2)  # Saly needs 10 eggs, Ben needs 14, and Ked needs half of what Ben needs
    eggs_per_month = eggs_per_week * 4  # There are 4 weeks in a month
    result = eggs_per_month
    return result

print(solution())