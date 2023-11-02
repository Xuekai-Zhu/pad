def solution():
    """Ella has 4 bags with 20 apples in each bag and six bags with 25 apples in each bag. If Ella sells 200 apples, how many apples does Ella has left?"""
    # Define the number of apples in each bag
    APPLES_PER_BAG_1 = 20
    APPLES_PER_BAG_2 = 25

    # Define the number of bags of each type
    BAGS_1 = 4
    BAGS_2 = 6

    # Calculate the total number of apples
    total_apples = (APPLES_PER_BAG_1 * BAGS_1) + (APPLES_PER_BAG_2 * BAGS_2)

    # Subtract the number of apples sold
    remaining_apples = total_apples - 200

    # Display the remaining number of apples
    result = remaining_apples
    return result

print(solution())