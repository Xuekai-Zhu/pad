def solution():
    """A park has 50 benches with a capacity of 4 people each. On a Sunday afternoon, 80 people were sitting on the benches. What's the number of available spaces on the benches that other people can sit on before the carrying capacity of the benches is full?"""
    num_benches = 50
    bench_capacity = 4
    num_people_sitting = 80
    max_people = num_benches * bench_capacity
    available_spaces = max_people - num_people_sitting
    result = available_spaces
    
    return result

print(solution())