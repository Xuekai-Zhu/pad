def solution():
    """A competition has racers competing on bicycles and tricycles to win a grand prize of $4000. If there are 40 people in the race, and 3/5 of them are riding on bicycles, how many wheels do the bicycles and tricycles in the race have combined?"""
    total_racers = 40
    bike_racers = int(total_racers * (3/5))
    trike_racers = total_racers - bike_racers
    bike_wheels = bike_racers * 2
    trike_wheels = trike_racers * 3
    total_wheels = bike_wheels + trike_wheels
    result = total_wheels
    return result

print(solution())