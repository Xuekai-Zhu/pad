def solution():
    wally_tickets = 400
    friends_share = 3/4

    # Calculate the total number of tickets given to the friends
    friend_tickets = wally_tickets * friends_share

    # Calculate the ratio of tickets shared between Jensen and Finley
    jensen_share = 4
    finley_share = 11
    total_share = jensen_share + finley_share

    # Calculate the number of tickets Finley gets
    finley_tickets = friend_tickets * (finley_share / total_share)
    result = finley_tickets
    return result

print(solution())