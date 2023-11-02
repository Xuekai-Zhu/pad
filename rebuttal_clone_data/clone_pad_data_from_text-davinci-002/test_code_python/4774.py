def solution():
    athlete1_longjump = 26
    athlete1_triplejump = 30
    athlete1_highjump = 7
    athlete2_longjump = 24
    athlete2_triplejump = 34
    athlete2_highjump = 8
    athlete1_avg = (athlete1_longjump + athlete1_triplejump + athlete1_highjump) / 3
    athlete2_avg = (athlete2_longjump + athlete2_triplejump + athlete2_highjump) / 3
    if athlete1_avg > athlete2_avg:
        result = "Athlete 1 has the highest average jump at " + str(athlete1_avg) + " feet."
    elif athlete2_avg > athlete1_avg:
        result = "Athlete 2 has the highest average jump at " + str(athlete2_avg) + " feet."
    else:
        result = "It's a tie!"
    return result

print(solution())