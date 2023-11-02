def solution():
    """Two boys, Ben and Leo, are fond of playing marbles. Ben has 56 marbles, while Leo has 20 more marbles than Ben. They put the marbles in one jar. How many marbles in the jar?"""
    # Define the number of marbles Ben has
    ben_marbles = 56

    # Calculate the number of marbles Leo has
    leo_marbles = ben_marbles + 20

    # Calculate the total number of marbles in the jar
    total_marbles = ben_marbles + leo_marbles

    # return the result
    result = total_marbles
    return result

print(solution())