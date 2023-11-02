def solution():
    
    # Define the number of matches Joey played on Monday
    monday_matches = 2

    # Define the number of matches Joey played on Friday
    friday_matches = 1

    # Define the number of matches Joey played on Saturday
    saturday_matches = monday_matches * 2

    # Calculate the total number of matches Joey played in one week
    total_matches = monday_matches + friday_matches + saturday_matches

    # Display the total number of matches
    result = total_matches
    return result

print(solution())