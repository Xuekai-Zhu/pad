def solution():
    
    total_racers = 40
    bike_racers = int(total_racers * (3/5))
    trike_racers = total_racers - bike_racers
    bike_wheels = bike_racers * 2
    trike_wheels = trike_racers * 3
    total_wheels = bike_wheels + trike_wheels
    result = total_wheels
    return result

print(solution())