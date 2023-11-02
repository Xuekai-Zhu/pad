def solution():
    """In a 5-day Fishing competition, Jackson was able to reel a total of 6 fishes per day, Jonah was able to reel 4 fishes per day and George was able to reel 8 fishes per day. How many fishes were they able to catch throughout the competition if they are on the same team?"""
    jackson_fishes_per_day = 6
    jonah_fishes_per_day = 4
    george_fishes_per_day = 8
    days = 5
    total_fishes = (jackson_fishes_per_day + jonah_fishes_per_day + george_fishes_per_day) * days
    result = total_fishes
    
    return result

print(solution())