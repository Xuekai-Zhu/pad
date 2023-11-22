def solution():
    
    # Define the number of matches played on Monday and Friday
    monday_matches = 2
    friday_matches = 1

    # Calculate the number of matches played on Saturday
    saturday_matches = monday_matches * 2

    # Calculate the total number of matches played in one week
    total_matches = monday_matches + friday_matches + saturday_matches

    # Display the total number of matches played in one week
    result = total_matches
    return result

print(solution())