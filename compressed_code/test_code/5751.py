def solution():
    
    wash_time = 10
    oil_time = 15
    tire_time = 30
    total_time = (wash_time * 9) + (oil_time * 6) + (tire_time * 2)
    total_hours = total_time / 60
    result = total_hours
    return result

print(solution())