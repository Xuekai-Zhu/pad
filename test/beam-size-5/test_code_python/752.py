def solution():
    
    # Define the total number of people on the council
    total_people = 33

    # Calculate the number of votes against the council
    against_votes = total_people // 3

    # Calculate the number of votes in favor of the new regulation
    favor_votes = against_votes * 2

    # Display the number of votes in favor of the new regulation
    result = favor_votes
    return result

print(solution())