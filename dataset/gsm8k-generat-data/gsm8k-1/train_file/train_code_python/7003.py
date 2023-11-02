def solution():
    """Jessy told eleven jokes this past Saturday, and Alan told seven jokes. If they doubled the number of jokes they told this past Saturday next Saturday, how many jokes would they have told in total together so far?"""
    jessy_jokes = 11
    alan_jokes = 7
    total_jokes = jessy_jokes + alan_jokes
    next_week_jessy_jokes = jessy_jokes * 2
    next_week_alan_jokes = alan_jokes * 2
    total_jokes += next_week_jessy_jokes + next_week_alan_jokes
    result = total_jokes
    return result

print(solution())