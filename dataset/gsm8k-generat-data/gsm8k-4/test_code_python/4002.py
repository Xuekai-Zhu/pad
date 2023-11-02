def solution():
    """Jeremy decides to take Tylenol because of the pain he is experiencing. He decides to take 1000 mg every 6 hours for 2 weeks. How many pills do they take if they are each 500 mg?"""
    # Define the dosage and duration of Tylenol intake
    dosage = 1000 # in mg
    interval = 6 # in hours
    duration = 14 # in days

    # Calculate the total number of pills taken
    days_in_hours = duration * 24
    pills_per_day = dosage / 500
    total_pills = pills_per_day * (days_in_hours // interval)

    # return the result
    result = int(total_pills)
    return result

print(solution())