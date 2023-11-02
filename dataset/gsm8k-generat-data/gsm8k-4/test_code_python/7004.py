def solution():
    """Jessy told eleven jokes this past Saturday, and Alan told seven jokes. If they doubled the number of jokes they told this past Saturday next Saturday, how many jokes would they have told in total together so far?"""
    # Define the number of jokes Jessy and Alan told this past Saturday
    jessy_jokes = 11
    alan_jokes = 7

    # Double the number of jokes they told for next Saturday
    jessy_jokes_next = jessy_jokes * 2
    alan_jokes_next = alan_jokes * 2

    # Calculate the total number of jokes they will tell next Saturday
    total_jokes_next = jessy_jokes_next + alan_jokes_next

    # Calculate the total number of jokes they have told so far
    total_jokes_so_far = (jessy_jokes + alan_jokes) + total_jokes_next

    # return the result
    result = total_jokes_so_far
    return result

print(solution())