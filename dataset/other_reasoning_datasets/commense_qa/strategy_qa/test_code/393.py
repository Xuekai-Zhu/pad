def solution():
    # Define the number of votes won in three presidential elections
    reagan_votes = 8000000
    roosevelt_votes = 11000000
    jefferson_votes = 162
    # Check if there were any greater landslides than the 1980 election
    if roosevelt_votes > reagan_votes or jefferson_votes > reagan_votes:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())