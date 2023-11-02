def solution():
    """Ella has 4 bags with 20 apples in each bag and six bags with 25 apples in each bag. If Ella sells 200 apples, how many apples does Ella has left?"""
    # Define the initial number of apples in each bag
    bag1 = 20
    bag2 = 20
    bag3 = 20
    bag4 = 20
    bag5 = 25
    bag6 = 25
    bag7 = 25
    bag8 = 25
    bag9 = 25
    bag10 = 25

    # Calculate the total number of apples
    total_apples = (bag1 + bag2 + bag3 + bag4 + bag5 + bag6 + bag7 + bag8 + bag9 + bag10)

    # Subtract the number of apples sold
    total_apples -= 200

    # Return the remaining number of apples
    result = total_apples
    return result

print(solution())