def solution():
    """Jessy told eleven jokes this past Saturday, and Alan told seven jokes. If they doubled the number of jokes they told this past Saturday next Saturday, how many jokes would they have told in total together so far?"""
    # Define the number of jokes Jessy and Alan told the past Saturday
    jessy_jokes = 11
    alan_jokes = 7

    # Double the number of jokes they will tell next Saturday
    jessy_jokes *= 2
    alan_jokes *= 2

    # Calculate the total number of jokes they will have told after next Saturday
    total_jokes = jessy_jokes + alan_jokes

    # Display the total number of jokes
    result = total_jokes
    return result

print(solution())