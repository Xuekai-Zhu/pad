def solution():
    # Calculate the number of experienced sailors
    experienced_sailors = 17 - 5

    # Calculate the hourly wage of the inexperienced sailors
    hourly_wage = 10

    # Calculate the hourly wage of an experienced sailor
    experienced_wage = hourly_wage * (1 + 1/5)

    # Calculate the total weekly earnings of the experienced sailors
    weekly_earnings = experienced_sailors * experienced_wage * 60

    # Calculate the total monthly earnings of the experienced sailors
    monthly_earnings = weekly_earnings * 4

    result = monthly_earnings
    return result

print(solution())