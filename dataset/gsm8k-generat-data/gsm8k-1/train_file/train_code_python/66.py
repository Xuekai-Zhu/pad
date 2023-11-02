def solution():
    """Jesse and Mia are competing in a week long race. They have one week to run 30 miles. On the first three days Jesse averages (2/3) of a mile. On day four she runs 10 miles. Mia averages 3 miles a day over the first 4 days. What is the average of their average that they have to run over the final three days?"""
    total_miles = 30
    jesse_miles_first_3_days = (2/3) * 3
    jesse_miles_day_4 = 10
    mia_miles_first_4_days = 3 * 4
    miles_left = total_miles - (jesse_miles_first_3_days + jesse_miles_day_4 + mia_miles_first_4_days)
    days_left = 3
    average_miles_needed = miles_left / days_left
    average_of_averages = (jesse_miles_first_3_days + jesse_miles_day_4 + mia_miles_first_4_days + average_miles_needed) / 4
    result = average_of_averages
    return result

print(solution())