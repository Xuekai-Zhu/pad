def solution():
    
    total_toys = 400
    worker1_toys = 6
    worker2_toys = 6
    worker3_toys = 4
    worker4_toys = 4
    worker5_toys = 20
    worker5_toys = total_toys - (worker1_toys + worker2_toys + worker3_toys)
    worker5_toys_per_hour = worker5_toys / 5
    result = worker5_toys_per_hour
    return result

print(solution())