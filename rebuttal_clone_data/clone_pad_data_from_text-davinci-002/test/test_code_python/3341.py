def solution():
    total_time = 30
    mary_rate = 10
    jess_rate = 7
    christina_rate = 4
    christina_time = total_time - 15
    total_balloons = mary_rate * total_time + jess_rate * total_time + christina_rate * christina_time
    result = total_balloons
    return result

print(solution())