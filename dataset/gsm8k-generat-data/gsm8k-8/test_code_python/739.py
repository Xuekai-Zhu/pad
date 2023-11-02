def solution():
    # Define the amount of blood needed in gallons
    blood_needed = 7

    # Convert 2 pints to gallons
    blood_per_person = 2/8

    # Calculate the number of people needed per day
    people_per_day = (blood_needed * 4) / blood_per_person / 7
    result = round(people_per_day)
    return result

print(solution())