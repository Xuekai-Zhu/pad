def solution():
    """A chocolate box contains 200 bars. Thomas and his 4 friends take 1/4 of the bars and decide to divide them equally between them. One of Thomas's friends doesn't like chocolate bars very much and returns 5 of his bars to the box. Later, his sister Piper comes home and takes 5 fewer bars than those taken in total by Thomas and his friends so she can also share with her friends. What's the total number of bars left in the box?"""
    # Define the initial number of bars in the box
    initial_bars = 200

    # Calculate the number of bars taken by Thomas and his friends
    taken_bars = initial_bars * 0.25

    # Calculate the number of bars left after being divided equally
    left_bars = taken_bars / 5

    # Subtract the bars returned by Thomas's friend
    left_bars -= 5

    # Calculate the number of bars taken by Piper
    piper_bars = taken_bars - 5

    # Calculate the total number of bars left in the box
    total_bars = initial_bars - taken_bars + left_bars + piper_bars

    # Display the total number of bars left in the box
    result = total_bars
    return result

print(solution())