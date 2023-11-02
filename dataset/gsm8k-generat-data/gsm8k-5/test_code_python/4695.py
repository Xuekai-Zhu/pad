def solution():
    indian_days = 3 * 7  # Nancy eats Indian food 3 times a week, so that's 3 * 7 days
    mexican_days = 2 * 7  # Nancy eats Mexican food 2 times a week, so that's 2 * 7 days
    other_days = 30 - indian_days - mexican_days  # Nancy eats other food on the remaining days of the month

    indian_antacids = 3 * indian_days  # Nancy takes 3 antacids per day when she eats Indian food
    mexican_antacids = 2 * mexican_days  # Nancy takes 2 antacids per day when she eats Mexican food
    other_antacids = other_days  # Nancy takes 1 antacid per day otherwise

    total_antacids = indian_antacids + mexican_antacids + other_antacids  # Total number of antacids Nancy takes per month
    result = total_antacids
    return result

print(solution())