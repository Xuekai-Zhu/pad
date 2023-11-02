def solution():
    # Define the initial number of bottles
    initial_bottles = 4 + 4

    # Calculate the total number of bottles after buying more
    total_bottles = initial_bottles + 5

    # Calculate the number of bottles left after drinking some
    bottles_left = total_bottles - 3
    result = bottles_left
    return result

print(solution())