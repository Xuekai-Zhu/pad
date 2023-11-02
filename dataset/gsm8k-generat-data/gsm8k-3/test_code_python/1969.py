def solution():
    """Stacy has 32 berries. Steve takes 4 of Stacy's berries, and still has 7 less berries than Stacy started with. How many berries did Steve start with?"""
    # Define the number of berries Stacy had initially
    stacy_initial = 32

    # Calculate the number of berries Steve has after taking 4
    steve_after = stacy_initial - 4

    # Calculate the number of berries Steve started with
    steve_initial = steve_after + 7

    # Display the number of berries Steve started with
    result = steve_initial
    return result

print(solution())