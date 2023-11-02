def solution():
    """To make a cherry pie, Veronica needs 3 pounds of pitted cherries.  There are 80 single cherries in one pound of cherries.   It takes 10 minutes to pit 20 cherries.  How many hours will it take Veronica to pit all the cherries?"""
    # Define the number of pounds of cherries needed
    cherries_needed = 3

    # Calculate the total number of cherries needed
    cherries_total = cherries_needed * 80

    # Calculate the number of batches of 20 cherries Veronica needs to pit
    batches = cherries_total // 20

    # Calculate the total time Veronica needs to pit all the cherries
    total_time = batches * 10 / 60

    # Display the total time in hours
    result = total_time
    return result

print(solution())