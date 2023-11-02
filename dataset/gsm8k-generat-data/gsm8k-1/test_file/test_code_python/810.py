def solution():
    """A new arcade opens up and Jack decides to play with his 3 friends. Jack can play a game with 1 quarter for 20 minutes. Two of his friends are significantly worse than him and can only play half as long. One of them is significantly better and can play for 1.5 times as long. They play for 4 hours. How much money is used?"""
    jack_play_time = 20
    friend1_play_time = jack_play_time / 2
    friend2_play_time = jack_play_time / 2
    friend3_play_time = jack_play_time * 1.5
    total_play_time = (jack_play_time + friend1_play_time + friend2_play_time + friend3_play_time) * 4 * 60
    money_used = total_play_time / 20
    result = money_used
    return result

print(solution())