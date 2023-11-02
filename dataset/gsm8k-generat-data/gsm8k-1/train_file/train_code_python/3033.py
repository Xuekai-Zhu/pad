def solution():
    """In the school election, Eliot got twice as many votes as Shaun, and Shaun got 5 times as many votes as Randy. If Randy got 16 votes, how many did Eliot get?"""
    randy_votes = 16
    shaun_votes = randy_votes * 5
    eliot_votes = shaun_votes * 2
    result = eliot_votes
    return result

print(solution())