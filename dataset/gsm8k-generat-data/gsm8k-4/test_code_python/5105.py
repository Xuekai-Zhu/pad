def solution():
    """Jerry is cutting up wood for his wood-burning stove. Each pine tree makes 80 logs, each maple tree makes 60 logs, and each walnut tree makes 100 logs. If Jerry cuts up 8 pine trees, 3 maple trees, and 4 walnut trees, how many logs does he get?"""
    # Define the number of logs each type of tree produces
    PINE_LOGS = 80
    MAPLE_LOGS = 60
    WALNUT_LOGS = 100

    # Define the number of each type of tree Jerry has
    NUM_PINE = 8
    NUM_MAPLE = 3
    NUM_WALNUT = 4

    # Calculate the total number of logs
    total_logs = (PINE_LOGS * NUM_PINE) + (MAPLE_LOGS * NUM_MAPLE) + (WALNUT_LOGS * NUM_WALNUT)

    # return the result
    result = total_logs
    return result

print(solution())