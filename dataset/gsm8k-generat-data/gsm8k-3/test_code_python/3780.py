def solution():
    """Janet counts 30 crows on the powerlines and 60% more hawks than crows. How many birds does she count total?"""
    # Define the number of crows Janet counted
    crows = 30

    # Calculate the number of hawks Janet counted
    hawks = int(crows * 1.6)

    # Calculate the total number of birds counted
    total_birds = crows + hawks

    # Display the total number of birds counted
    result = total_birds
    return result

print(solution())