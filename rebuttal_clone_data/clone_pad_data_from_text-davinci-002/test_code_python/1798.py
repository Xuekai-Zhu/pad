def solution():
    initial_bench_press = 500
    injury_percentage = 80
    weight_lost = initial_bench_press * (injury_percentage / 100)
    current_bench_press = initial_bench_press - weight_lost
    percent_increase = 300
    weight_gained = current_bench_press * (percent_increase / 100)
    result = current_bench_press + weight_gained
    
    return result

print(solution())