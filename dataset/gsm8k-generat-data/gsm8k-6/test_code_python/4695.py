def solution():
    # Calculate the total number of antacids Nancy takes per week
    antacids_per_week = 3*3 + 2*2 + 2*(7-3-2)  # Nancy eats Indian three times a week and Mexican twice a week, and takes 1 antacid per day otherwise

    # Calculate the total number of antacids Nancy takes per month
    antacids_per_month = antacids_per_week * 4  # assuming there are 4 weeks in a month

    result = antacids_per_month
    return result

print(solution())