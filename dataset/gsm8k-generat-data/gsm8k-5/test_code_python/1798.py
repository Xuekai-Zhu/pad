def solution():
    starting_bench_press = 500  # John started with a 500-pound bench press
    reduced_bench_press = starting_bench_press * 0.2  # After the injury, his bench press went down 80%
    recovered_bench_press = reduced_bench_press * 3  # After training, he tripled the weight he can bench

    # Calculate John's current bench press
    current_bench_press = starting_bench_press + recovered_bench_press
    result = current_bench_press
    return result

print(solution())