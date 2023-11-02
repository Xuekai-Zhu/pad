def solution():
    """In the school election, Eliot got twice as many votes as Shaun, and Shaun got 5 times as many votes as Randy. If Randy got 16 votes, how many did Eliot get?"""
    randy_votes = 16
    shaun_votes = 5 * randy_votes
    eliot_votes = 2 * shaun_votes
    result = eliot_votes
    return result

print(solution())