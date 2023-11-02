def solution():
    """A park has 50 benches with a capacity of 4 people each. On a Sunday afternoon, 80 people were sitting on the benches. What's the number of available spaces on the benches that other people can sit on before the carrying capacity of the benches is full?"""
    # Define the number of benches and their capacity
    num_benches = 50
    bench_capacity = 4

    # Calculate the total number of people that can sit on the benches
    total_capacity = num_benches * bench_capacity

    # Calculate the number of people currently sitting on the benches
    num_people = 80

    # Calculate the number of available spaces on the benches
    available_spaces = total_capacity - num_people

    # Display the result
    result = available_spaces
    return result

print(solution())