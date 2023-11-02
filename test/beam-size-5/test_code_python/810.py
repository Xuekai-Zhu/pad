def solution():
    
    jack_play_time = 0.25 * 20
    jack_friends_play_time = jack_play_time * 2
    jack_friends_play_time_1 = jack_friends_play_time / 2
    jack_friends_play_time_2 = jack_friends_play_time / 2
    jack_friends_play_time_3 = jack_friends_play_time / 1.5
    total_play_time_1 = jack_friends_play_time_1 * 4
    total_play_time_2 = jack_friends_play_time_2 * 4
    total_play_time_3 = jack_friends_play_time_3 * 4
    total_play_money = total_play_time_1 + total_play_time_2 + total_play_time_3
    result = total_play_money
    return result

print(solution())