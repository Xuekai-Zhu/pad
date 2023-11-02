def solution():
    """Jerry is cutting up wood for his wood-burning stove. Each pine tree makes 80 logs, each maple tree makes 60 logs, and each walnut tree makes 100 logs. If Jerry cuts up 8 pine trees, 3 maple trees, and 4 walnut trees, how many logs does he get?"""
    # Define the number of logs each type of tree makes
    PINE_LOGS = 80
    MAPLE_LOGS = 60
    WALNUT_LOGS = 100

    # Define the number of trees cut
    pine_trees = 8
    maple_trees = 3
    walnut_trees = 4

    # Calculate the total number of logs
    total_logs = (pine_trees * PINE_LOGS) + (maple_trees * MAPLE_LOGS) + (walnut_trees * WALNUT_LOGS)

    # Display the total number of logs
    result = total_logs
    return result

print(solution())