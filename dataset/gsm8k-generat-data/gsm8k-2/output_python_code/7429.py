def solution():
    """A park has 50 benches with a capacity of 4 people each. On a Sunday afternoon, 80 people were sitting on the benches. What's the number of available spaces on the benches that other people can sit on before the carrying capacity of the benches is full?"""
    total_benches = 50
    capacity_per_bench = 4
    people_sitting = 80
    total_capacity = total_benches * capacity_per_bench
    occupied_capacity = people_sitting
    available_capacity = total_capacity - occupied_capacity
    result = available_capacity
    return result

print(solution())