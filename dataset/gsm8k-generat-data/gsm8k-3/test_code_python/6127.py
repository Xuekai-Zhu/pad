def solution():
    """Every time Janet folds her blanket its thickness doubles. If it starts out 3 inches thick, how thick will it be after 4 foldings?"""
    # Define the starting thickness
    thickness = 3

    # Fold the blanket 4 times
    for i in range(4):
        thickness *= 2

    # Display the final thickness
    result = thickness
    return result

print(solution())