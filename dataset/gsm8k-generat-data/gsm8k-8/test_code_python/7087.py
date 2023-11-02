def solution():
    # Define the total hours Sangita needs to fly
    total_hours = 1500

    # Define the hours Sangita has already flown
    flown_hours = 50 + 9 + 121

    # Define the remaining hours Sangita needs to fly
    remaining_hours = total_hours - flown_hours

    # Define the number of months Sangita has to complete her goal
    num_months = 6

    # Calculate the average hours Sangita needs to fly per month
    hours_per_month = remaining_hours / num_months

    result = hours_per_month
    return result

print(solution())