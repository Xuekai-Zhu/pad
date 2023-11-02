def solution():
    starting_bench_press = 500

    # Calculate the bench press after the 80% decrease
    decreased_bench_press = starting_bench_press * 0.2

    # Calculate the bench press after tripling the decreased bench press
    final_bench_press = decreased_bench_press * 3

    result = final_bench_press
    return result

print(solution())