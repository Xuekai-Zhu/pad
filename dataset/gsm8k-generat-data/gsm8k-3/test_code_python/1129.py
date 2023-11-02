def solution():
    """Martin is casting three bells for the church's belfry. The first bell takes 50 pounds of bronze, the second bell is twice the size of the first bell, and the third bell is four times the size of the second bell. How much bronze does he need total?"""
    # Define the weight of bronze for the first bell
    bell1_bronze = 50

    # Calculate the weight of bronze for the second bell
    bell2_bronze = bell1_bronze * 2

    # Calculate the weight of bronze for the third bell
    bell3_bronze = bell2_bronze * 4

    # Calculate the total weight of bronze needed for all three bells
    total_bronze = bell1_bronze + bell2_bronze + bell3_bronze

    # Display the total weight of bronze needed
    result = total_bronze
    return result

print(solution())