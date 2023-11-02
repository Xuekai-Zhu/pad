def solution():
    """There are three machines in a factory. Machine A can put caps on 12 bottles in 1 minute. Machine B can put caps to 2 fewer bottles than Machine A. Machine C can put caps to 5 more bottles than Machine B. How many bottles can those three machines put caps on in 10 minutes?"""
    # Define the number of bottles per minute for each machine
    bottles_per_min_A = 12
    bottles_per_min_B = bottles_per_min_A - 2
    bottles_per_min_C = bottles_per_min_B + 5

    # Calculate the total number of bottles each machine can cap in 10 minutes
    bottles_cap_A = bottles_per_min_A * 10
    bottles_cap_B = bottles_per_min_B * 10
    bottles_cap_C = bottles_per_min_C * 10

    # Calculate the total number of bottles all three machines can cap in 10 minutes
    total_bottles_cap = bottles_cap_A + bottles_cap_B + bottles_cap_C

    # return the result
    result = total_bottles_cap
    return result

print(solution())