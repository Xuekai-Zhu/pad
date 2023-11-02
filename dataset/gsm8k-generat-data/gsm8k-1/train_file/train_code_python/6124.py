def solution():
    """Four athletes joined a relay race. Athlete 1 ran for 55 seconds, athlete 2 ran 10 seconds more than athlete 1, athlete 3 ran 15 seconds less than athlete 2, and athlete four finished it 25 seconds less than athlete 1. How long, in seconds, did it take them to finish the relay race?"""
    athlete_1 = 55
    athlete_2 = athlete_1 + 10
    athlete_3 = athlete_2 - 15
    athlete_4 = athlete_1 - 25
    total_time = athlete_1 + athlete_2 + athlete_3 + athlete_4
    result = total_time
    return result

print(solution())