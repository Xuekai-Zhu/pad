def solution():
    hours_per_volunteering_session = 3  # John volunteers for 3 hours at a time
    sessions_per_month = 2  # John volunteers twice a month
    months_per_year = 12  # There are 12 months in a year

    # Calculate the total number of hours John volunteers per year
    total_hours = hours_per_volunteering_session * sessions_per_month * months_per_year
    result = total_hours
    return result

print(solution())