def solution():
    """There are three machines in a factory. Machine A can put caps on 12 bottles in 1 minute. Machine B can put caps to 2 fewer bottles than Machine A. Machine C can put caps to 5 more bottles than Machine B. How many bottles can those three machines put caps on in 10 minutes?"""
    machine_a_rate = 12
    machine_b_rate = machine_a_rate - 2
    machine_c_rate = machine_b_rate + 5
    total_bottles = (machine_a_rate + machine_b_rate + machine_c_rate) * 10
    result = total_bottles
    return result

print(solution())