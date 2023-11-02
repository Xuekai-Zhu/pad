def solution():
    """I have purchased 5 blue apples at the store. Suppose my neighbor gives me twice as many yellow apples as I have blue ones, and then I give my son 1/5 of the total number of apples; how many apples do I have now?"""
    # Define the number of blue apples purchased
    blue_apples = 5

    # Calculate the number of yellow apples received from neighbor
    yellow_apples = blue_apples * 2

    # Calculate the total number of apples
    total_apples = blue_apples + yellow_apples

    # Calculate the number of apples given to son
    son_apples = total_apples / 5

    # Calculate the remaining number of apples
    remaining_apples = total_apples - son_apples

    # Display the remaining number of apples
    result = remaining_apples
    return result

print(solution())