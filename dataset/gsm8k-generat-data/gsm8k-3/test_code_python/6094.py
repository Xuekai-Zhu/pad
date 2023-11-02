def solution():
    """Walter goes to the zoo, where he spends a certain amount of time looking at the seals, eight times as long looking at the penguins, and 13 minutes looking at the elephants. If he spent 2 hours and 10 minutes at the zoo, how many minutes did he spent looking at the seals?"""
    # Define the time spent looking at the elephants
    ELEPHANT_TIME = 13

    # Calculate the total time spent at the zoo in minutes
    total_time = 2 * 60 + 10

    # Calculate the time spent looking at the penguins
    penguin_time = 8 * seal_time

    # Calculate the time spent looking at the seals
    seal_time = (total_time - ELEPHANT_TIME) / (1 + 8 + 1/60)

    # Display the time spent looking at the seals
    result = seal_time
    return result

print(solution())