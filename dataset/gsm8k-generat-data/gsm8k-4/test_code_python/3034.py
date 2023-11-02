def solution():
    """In the school election, Eliot got twice as many votes as Shaun, and Shaun got 5 times as many votes as Randy.
    If Randy got 16 votes, how many did Eliot get?"""
    
    # Define the number of votes Randy got
    randy_votes = 16

    # Calculate the number of votes Shaun got
    shaun_votes = randy_votes * 5

    # Calculate the number of votes Eliot got
    eliot_votes = shaun_votes * 2

    result = eliot_votes
    return result

print(solution())