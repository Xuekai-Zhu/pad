def solution():
    
    # Define the total number of pupils
    total_pupils = 40

    # Calculate the number of pupils who likes blue
    blue_pupils = total_pupils / 2

    # Calculate the number of pupils who did not like blue
    remaining_pupils = total_pupils - blue_pupils

    # Calculate the number of pupils who likes green
    green_pupils = remaining_pupils / 4

    # Calculate the number of pupils who likes yellow
    yellow_pupils = remaining_pupils - green_pupils

    # Display the number of pupils who likes yellow
    result = yellow_pupils
    return result

print(solution())