def solution():
    # Define the weights of each bell
    bell1_weight = 50
    bell2_weight = 2 * bell1_weight
    bell3_weight = 4 * bell2_weight

    # Calculate the total amount of bronze needed
    total_bronze = bell1_weight + bell2_weight + bell3_weight
    result = total_bronze
    return result

print(solution())