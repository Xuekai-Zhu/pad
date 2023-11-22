def solution():
    
    # Define the number of people and eggs consumed per day
    num_people = 5
    eggs_per_person_per_day = [3, 3, 2]

    # Calculate the total number of eggs consumed per day
    total_eggs_per_day = sum(eggs_per_person_per_day)

    # Calculate the total number of eggs consumed in a week
    total_eggs_per_week = total_eggs_per_day * 7

    # Display the total number of eggs consumed in a week
    result = total_eggs_per_week
    return result

print(solution())