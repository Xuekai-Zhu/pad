def solution():
    
    # Define the total number of voters
    total_voters = 100

    # Calculate the number of votes received by candidate A
    votes_A = total_voters * 0.2

    # Calculate the number of votes received by candidate B
    votes_B = votes_A * 1.5

    # Calculate the number of votes received by candidate C
    votes_C = total_voters - votes_A - votes_B

    # Display the number of votes received by candidate C
    result = votes_C
    return result

print(solution())