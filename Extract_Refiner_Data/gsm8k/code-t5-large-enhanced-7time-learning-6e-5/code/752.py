def solution():
    
    # Define the number of votes against the old regulation
    old_votes = 0

    # Calculate the number of votes passing with the old regulation
    new_votes = 2 * old_votes

    # Calculate the number of votes in favor of the new regulation
    new_votes_favor = new_votes * 2

    # Display the number of votes in favor of the new regulation
    result = new_votes_favor
    return result

print(solution())