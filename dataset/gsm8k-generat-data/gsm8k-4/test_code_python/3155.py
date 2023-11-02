def solution():
    """A chocolate box contains 200 bars. Thomas and his 4 friends take 1/4 of the bars and decide to divide them equally between them. One of Thomas's friends doesn't like chocolate bars very much and returns 5 of his bars to the box. Later, his sister Piper comes home and takes 5 fewer bars than those taken in total by Thomas and his friends so she can also share with her friends. What's the total number of bars left in the box?"""
    # Define the initial number of chocolate bars
    initial_bars = 200

    # Calculate the number of bars taken by Thomas and his friends
    friends_bars = initial_bars * (1/4)
    total_bars = friends_bars + 5

    # Calculate the number of bars left after one friend returns 5 bars
    remaining_bars = total_bars - 5

    # Calculate the number of bars taken by Piper
    piper_bars = (total_bars - 5) / 5

    # Calculate the total number of bars left in the box
    total_left = initial_bars - friends_bars - remaining_bars - piper_bars

    # Return the result
    result = total_left
    return result

print(solution())