def solution():
    # Define the number of people who came in to run on the treadmill and who left the gym
    treadmill_people = 5
    left_people = 2

    # Calculate the total number of people who were in the gym after the changes
    total_people = 19

    # Subtract the number of people who came in and who left from the total number of people to find the initial number of weightlifters
    weightlifters = total_people - treadmill_people - left_people
    result = weightlifters
    return result

print(solution())