def solution():
    # Calculate the total runs of Billy and Tiffany in a week
    total_runs_Billy = 1 + 1 + 1 + 1 + 1 + 1 + 1  # Billy runs 1 mile each day for 7 days
    total_runs_Tiffany = 2 + 2 + 2 + 1/3 + 1/3 + 1/3 + 0  # Tiffany runs 2 miles for 3 days and 1/3 mile for 3 days and takes Saturday off

    # Calculate how many miles Billy needs to run on Saturday to tie Tiffany
    miles_to_tie = total_runs_Tiffany - total_runs_Billy

    result = miles_to_tie
    return result

print(solution())