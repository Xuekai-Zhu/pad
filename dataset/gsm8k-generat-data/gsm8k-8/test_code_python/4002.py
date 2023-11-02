def solution():
    # Define the amount and frequency of Tylenol taken
    dosage = 1000   # in mg
    frequency = 6   # in hours
    duration = 14   # in days

    # Convert duration of 2 weeks to hours
    duration_hours = duration * 24 * 7

    # Calculate the total amount of Tylenol taken in mg
    total_tylenol = dosage * (duration_hours // frequency)

    # Calculate the number of pills taken (assuming each pill is 500 mg)
    num_pills = total_tylenol // 500
    
    result = num_pills
    return result

print(solution())