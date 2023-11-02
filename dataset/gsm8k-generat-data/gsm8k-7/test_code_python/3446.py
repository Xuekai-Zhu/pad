def solution():
    total_prize = 4000
    num_racers = 40
    bike_ratio = 3/5
    trike_ratio = 2/5
    num_bikers = round(num_racers * bike_ratio)
    num_trikers = num_racers - num_bikers
    total_wheels = (num_bikers * 2) + (num_trikers * 3)
    result = total_wheels
    return result

print(solution())