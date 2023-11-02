def solution():
    
    # Define the total number of people and the percentage of people who receive interviews
    total_people = 100
    interviews_percentage = 0.3

    # Calculate the number of people who receive interviews
    interviews = total_people * interviews_percentage

    # Calculate the number of people who receive a job offer
    offerers = total_people * 0.2

    # Calculate the number of people who accept the position
    position = offerers / 3

    # Display the number of people who accept the position
    result = position
    return result

print(solution())