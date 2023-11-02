def solution():
    # Calculate the total minutes Jeff should have run for the week
    total_minutes = 5 * 60

    # Subtract 20 minutes from Thursday's run and add 10 minutes to Friday's run
    thursday_run = (60 - 20)
    friday_run = (60 + 10)

    # Calculate the total minutes Jeff actually ran for the week
    actual_minutes = thursday_run + friday_run + (3 * 60)

    result = actual_minutes
    return result

print(solution())