def solution():
    """Martin is casting three bells for the church's belfry. The first bell takes 50 pounds of bronze, the second bell is twice the size of the first bell, and the third bell is four times the size of the second bell. How much bronze does he need total?"""
    # Define the amount of bronze needed for the first bell
    bronze_bell1 = 50

    # Define the amount of bronze needed for the second bell (twice the size of the first bell)
    bronze_bell2 = bronze_bell1 * 2

    # Define the amount of bronze needed for the third bell (four times the size of the second bell)
    bronze_bell3 = bronze_bell2 * 4

    # Calculate the total amount of bronze needed
    total_bronze = bronze_bell1 + bronze_bell2 + bronze_bell3

    # Return the result
    result = total_bronze
    return result

print(solution())