def solution():
    
    # Define the number of days Sofie will walk
    days_sofie = 7

    # Define the number of miles Sofie plans to walk every day
    miles_per_day = 10

    # Calculate the total number of miles Sofie will walk in 7 days
    total_miles_sofie = days_sofie * miles_per_day

    # Calculate the number of miles Brian will walk in 7 days
    miles_per_day_brian = total_miles_sofie / 2

    # Calculate the number of miles Brian will walk in 7 days
    miles_per_day_7_days = miles_per_day_brian * 7

    # Display the number of miles Brian will walk in 7 days
    result = miles_per_day_7_days
    return result

print(solution())