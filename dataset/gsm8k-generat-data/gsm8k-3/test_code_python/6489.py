def solution():
    """A squirrel had stashed 210 acorns to last him the three winter months. It divided the pile into thirds, one for each month, and then took some from each third, leaving 60 acorns for each winter month. The squirrel combined the ones it took to eat in the first cold month of spring before plants were in bloom again. How many acorns does the squirrel have to eat at the beginning of spring?"""
    # Define the total number of acorns stashed by the squirrel
    total_acorns = 210

    # Divide the pile into thirds
    third = total_acorns / 3

    # Calculate the number of acorns left in each third after the squirrel took some
    remaining_third = third - 60

    # Calculate the total number of acorns left for the squirrel to eat in spring
    spring_acorns = remaining_third * 3

    # Display the number of acorns the squirrel has to eat in spring
    result = spring_acorns
    return result

print(solution())