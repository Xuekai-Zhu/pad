def solution():
    """A squirrel had stashed 210 acorns to last him the three winter months. It divided the pile into thirds, one for each month, and then took some from each third, leaving 60 acorns for each winter month. The squirrel combined the ones it took to eat in the first cold month of spring before plants were in bloom again. How many acorns does the squirrel have to eat at the beginning of spring?"""
    # Define the total number of acorns
    total_acorns = 210

    # Calculate the number of acorns per winter month
    acorns_per_month = total_acorns / 3

    # Calculate the number of acorns left after the squirrel took some from each third
    remaining_acorns = total_acorns - (3 * 60)

    # Calculate the number of acorns the squirrel took to eat in the first cold month of spring
    spring_acorns = (acorns_per_month - 60) * 3

    # Calculate the total number of acorns the squirrel has to eat at the beginning of spring
    total_spring_acorns = spring_acorns + remaining_acorns

    # Return the result
    result = total_spring_acorns
    return result

print(solution())