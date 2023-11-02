def solution():
 
    first_podcast = 45
    second_podcast = first_podcast * 2
    third_podcast = 105
    fourth_podcast = 60
    total_time = first_podcast + second_podcast + third_podcast + fourth_podcast
    next_podcast = 360 - total_time
 
    return next_podcast

print(solution())