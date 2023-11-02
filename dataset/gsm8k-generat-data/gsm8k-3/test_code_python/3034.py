def solution():
    """In the school election, Eliot got twice as many votes as Shaun, and Shaun got 5 times as many votes as Randy. If Randy got 16 votes, how many did Eliot get?"""
    # Define the number of votes Randy got
    randy_votes = 16

    # Calculate Shaun's number of votes
    shaun_votes = randy_votes * 5

    # Calculate Eliot's number of votes
    eliot_votes = shaun_votes * 2

    # Display Eliot's number of votes
    result = eliot_votes
    return result

print(solution())