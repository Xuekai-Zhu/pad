def solution():
    
    total_campers = 96
    boys = total_campers * 2 / 3
    girls = total_campers * 1 / 3
    boys_toast = boys * 0.5
    girls_toast = girls * 0.75
    total_toast = boys_toast + girls_toast
    result = total_toast
    return result

print(solution())