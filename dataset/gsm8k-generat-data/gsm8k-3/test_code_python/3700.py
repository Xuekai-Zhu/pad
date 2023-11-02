def solution():
    """There are three machines in a factory. Machine A can put caps on 12 bottles in 1 minute. Machine B can put caps to 2 fewer bottles than Machine A. Machine C can put caps to 5 more bottles than Machine B. How many bottles can those three machines put caps on in 10 minutes?"""
    # Calculate the number of bottles each machine can cap in 1 minute
    machine_a = 12
    machine_b = machine_a - 2
    machine_c = machine_b + 5

    # Calculate the total number of bottles capped in 10 minutes
    total_bottles = (machine_a + machine_b + machine_c) * 10

    # Display the total number of bottles capped
    result = total_bottles
    return result

print(solution())