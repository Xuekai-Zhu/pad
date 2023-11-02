def solution():
    
    time_per_lily = 5
    time_per_rose = 7
    time_per_orchid = 3
    time_per_vine = 2
    num_lilies = 17
    num_roses = 10
    num_orchids = 6
    num_vines = 20
    total_time = (time_per_lily * num_lilies) + (time_per_rose * num_roses) + (time_per_orchid * num_orchids) + (time_per_vine * num_vines)
    result = total_time
    return result

print(solution())