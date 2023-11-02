def solution():
    """At 8:00, 5000 people lined up at a polling station to cast their vote on election day. By midday 2/5 of the people had voted and by 16:00 2/3 of the remaining people had voted. What's the number of those who had not voted by 16:00?"""
    initial_voters = 5000
    midday_voters = initial_voters * (2/5)
    remaining_voters = initial_voters - midday_voters
    afternoon_voters = remaining_voters * (2/3)
    not_voted = initial_voters - midday_voters - afternoon_voters
    result = not_voted
    
    return result

print(solution())