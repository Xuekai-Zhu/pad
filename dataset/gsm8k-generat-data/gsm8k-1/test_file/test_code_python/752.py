def solution():
    """A council met to vote on a new regulation. The vote passed with twice as many votes in favor of the new regulation as there were against it. If there are 33 people on the council, what was the number of votes in favor of the new regulation?"""
    total_people = 33
    votes_against = total_people / 3
    votes_for = votes_against * 2
    result = votes_for
    return result

print(solution())