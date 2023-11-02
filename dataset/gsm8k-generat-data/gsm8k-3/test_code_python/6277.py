def solution():
    """Adam, Andrew and Ahmed all raise goats.  Adam has 7 goats.  Andrew has 5 more than twice as many goats as Adam.  Ahmed has 6 fewer goats than Andrew.  How many goats does Ahmed have?"""
    # Define the number of goats Adam has
    adam_goats = 7

    # Define the number of goats Andrew has
    andrew_goats = 5 + 2 * adam_goats

    # Define the number of goats Ahmed has
    ahmed_goats = andrew_goats - 6

    # Display the number of goats Ahmed has
    result = ahmed_goats
    return result

print(solution())