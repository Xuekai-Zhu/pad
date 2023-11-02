def solution():
    """Ben has 8 apples more than Phillip does. Tom has three eighths as many apples at Ben has. If Phillip has 40 apples, how many apples does Tom have?"""
    # Define the number of apples Phillip has
    phillip_apples = 40

    # Calculate the number of apples Ben has
    ben_apples = phillip_apples + 8

    # Calculate the number of apples Tom has
    tom_apples = ben_apples * (3/8)

    # Display the number of apples Tom has
    result = tom_apples
    return result

print(solution())