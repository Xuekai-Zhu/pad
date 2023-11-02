def solution():
    # Find the rate of production of each machine
    rate_per_machine = 10  # 2 machines can make 10 cell phones each minute

    # Find the number of machines needed to make 50 cell phones per minute
    required_machines = 50 / rate_per_machine

    result = required_machines
    return result

print(solution())