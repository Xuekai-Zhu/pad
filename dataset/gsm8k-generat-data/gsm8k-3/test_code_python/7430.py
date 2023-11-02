def solution():
    """A park has 50 benches with a capacity of 4 people each. On a Sunday afternoon, 80 people were sitting on the benches. What's the number of available spaces on the benches that other people can sit on before the carrying capacity of the benches is full?"""
    # Define the number of benches and their capacity
    benches = 50
    capacity = 4

    # Calculate the number of people sitting on the benches
    sitting = 80

    # Calculate the total capacity of all the benches
    total_capacity = benches * capacity

    # Calculate the number of available spaces on the benches
    available = total_capacity - sitting

    # Display the number of available spaces
    result = available
    return result

print(solution())