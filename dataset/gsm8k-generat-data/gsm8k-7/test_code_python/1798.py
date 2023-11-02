def solution():
    initial_bench_press = 500
    decreased_percentage = 0.80  # 80% decrease
    final_bench_press = initial_bench_press * (1 - decreased_percentage)

    increased_multiplier = 3
    current_bench_press = final_bench_press * increased_multiplier
    result = current_bench_press
    return result

print(solution())