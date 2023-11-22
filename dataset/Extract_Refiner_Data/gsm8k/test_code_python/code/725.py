def solution():
    
    # Define the initial number of people
    initial_votes = 5000

    # Calculate the number of people who had voted by midday
    midday_votes = initial_votes * (2/5)

    # Calculate the number of people who had voted by 16:00
    16_votes = initial_votes - midday_votes

    # Calculate the number of people who had not voted by 16:00
    not_voted_by_16_votes = 16_votes * (2/3)

    # Display the number of people who had not voted by 16:00
    result = not_voted_by_16_votes
    return result

print(solution())