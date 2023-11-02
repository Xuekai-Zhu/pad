def solution():
    """A chocolate box contains 200 bars. Thomas and his 4 friends take 1/4 of the bars and decide to divide them equally between them. One of Thomas's friends doesn't like chocolate bars very much and returns 5 of his bars to the box. Later, his sister Piper comes home and takes 5 fewer bars than those taken in total by Thomas and his friends so she can also share with her friends. What's the total number of bars left in the box?"""
    total_bars = 200
    num_friends = 4
    fraction_taken = 1/4
    bars_taken = fraction_taken * total_bars
    bars_per_person = bars_taken / (num_friends + 1)
    thomas_bars = bars_per_person
    friend_bars = bars_per_person
    piper_bars = thomas_bars + friend_bars - 5
    total_bars -= bars_taken
    total_bars += (thomas_bars + friend_bars + piper_bars)
    result = total_bars
    return result

print(solution())