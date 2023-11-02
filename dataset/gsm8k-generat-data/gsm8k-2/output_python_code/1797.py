def solution():
    """John injures his shoulder while lifting weights. After the injury, his bench press goes down 80%. After a bit of training, he manages to triple the weight he can bench. If he started with a 500-pound bench press, what is it now?"""
    initial_bench_press = 500
    after_injury_press = initial_bench_press * 0.2
    final_press = after_injury_press * 3
    result = final_press
    return result

print(solution())