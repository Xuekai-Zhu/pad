def solution():
    """A chocolate box contains 200 bars. Thomas and his 4 friends take 1/4 of the bars and decide to divide them equally between them. 
    One of Thomas's friends doesn't like chocolate bars very much and returns 5 of his bars to the box. Later, his sister Piper comes home and 
    takes 5 fewer bars than those taken in total by Thomas and his friends so she can also share with her friends. What's the total number of bars left in the box?"""
    
    total_bars = 200
    thomas_and_friends = total_bars // 4
    number_of_people = 5
    bars_per_person = thomas_and_friends // number_of_people
    bars_returned = 5
    bars_taken_by_piper = thomas_and_friends - bars_returned - 5
    total_bars_left = total_bars - thomas_and_friends + bars_returned - bars_taken_by_piper
    
    result = total_bars_left
    return result

print(solution())