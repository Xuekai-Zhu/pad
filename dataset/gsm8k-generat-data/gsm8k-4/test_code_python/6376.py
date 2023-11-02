def solution():
    """Tom attends a party that collects $2000. Half the school attended and the school had 400 people. How much would they have made if 300 people attended?"""
    # Define the number of people who attended Tom's party and the total amount collected
    tom_attendance = 200
    total_collected = 2000

    # Calculate the amount collected per person
    per_person = total_collected / tom_attendance

    # Calculate the amount that would be collected if 300 people attended
    new_attendance = 300
    new_total = new_attendance * per_person

    # return the result
    result = new_total
    return result

print(solution())