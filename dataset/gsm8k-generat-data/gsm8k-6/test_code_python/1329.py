def solution():
    total_votes = 1150
    john_votes = 150
    remaining_votes = total_votes - john_votes
    
    # Calculate the number of votes James gets
    james_votes = 0.7 * remaining_votes
    
    # Calculate the number of votes the third guy gets
    third_guy_votes = remaining_votes - james_votes
    
    # Calculate the difference in votes between John and the third guy
    diff_votes = third_guy_votes - john_votes
    
    result = diff_votes
    return result

print(solution())