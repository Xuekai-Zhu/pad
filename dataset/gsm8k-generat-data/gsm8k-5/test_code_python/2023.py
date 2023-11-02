def solution():
    beth_age = 18
    sister_age = 5
    age_diff = beth_age - sister_age  # Calculate the age difference between Beth and her sister
    years_until_twice = age_diff  # Beth needs to wait for the age difference to double
    while beth_age + years_until_twice != 2 * (sister_age + years_until_twice):  # Check if the age difference has doubled yet
        years_until_twice += 1  # Increment the years by 1 until the age difference doubles
    result = years_until_twice
    return result

print(solution())