def solution():
    # Set variables
    penguin_time = 8 * seal_time
    elephant_time = 13
    total_time = 2*60 + 10

    # Calculate seal time
    time_spent = seal_time + penguin_time + elephant_time
    seal_time = (total_time - time_spent)

    result = seal_time
    return result

print(solution())