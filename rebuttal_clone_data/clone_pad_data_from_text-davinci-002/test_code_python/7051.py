def solution():
    total_minnows = 600
    minnows_per_prize = 3
    people_playing = 800
    people_winning = people_playing * .15
    minnows_needed = people_winning * minnows_per_prize
    minnows_leftover = total_minnows - minnows_needed
    
    result = minnows_leftover

    return result

print(solution())