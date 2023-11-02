def solution():
    """To make a cherry pie, Veronica needs 3 pounds of pitted cherries. There are 80 single cherries in one pound of cherries. It takes 10 minutes to pit 20 cherries. How many hours will it take Veronica to pit all the cherries?"""
    # Define the number of pounds of cherries needed
    pounds_of_cherries = 3

    # Calculate the total number of single cherries needed
    single_cherries = pounds_of_cherries * 80

    # Calculate the number of 20-cherries batches Veronica needs to pit
    batches = single_cherries / 20

    # Calculate the total time needed to pit all the cherries
    time = batches * 10 / 60

    # Return the result in hours
    result = time
    return result

print(solution())