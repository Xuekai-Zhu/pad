def solution():
    """Loraine makes wax sculptures of animals. Large animals take four sticks of wax and small animals take two sticks. She made three times as many small animals as large animals, and she used 12 sticks of wax for small animals. How many sticks of wax did Loraine use to make all the animals?"""
    # Define the number of large animals
    large_animals = None

    # Define the number of small animals
    small_animals = None

    # Define the total number of sticks of wax used
    total_sticks = None

    small_sticks = 12

    #Calculate the number of small animals
    small_animals = small_sticks // 2

    # Calculate the number of large animals
    large_animals = small_animals // 3

    # Calculate the total number of sticks of wax used
    total_sticks = (large_animals * 4) + (small_animals * 2)

    result = total_sticks
    return result

print(solution())