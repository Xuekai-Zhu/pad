def solution():
    initial_height = 100
    growth_rate = 0.1
    end_year = 2019
    start_year = 2017

    # Calculate how many years have passed since 2017
    time_elapsed = end_year - start_year

    # Calculate the final height of the tree after the specified time has elapsed
    final_height = initial_height * ((1 + growth_rate) ** time_elapsed)

    # Calculate the amount of growth of the tree
    growth = final_height - initial_height

    result = growth
    return result

print(solution())