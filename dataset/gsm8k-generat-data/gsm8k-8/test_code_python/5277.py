def solution():
    # Define the total number of apples picked
    total_apples = 34

    # Calculate the number of ripe apples
    ripe_apples = total_apples - 6

    # Calculate the number of pies they can make
    pies = ripe_apples // 4

    result = pies
    return result

print(solution())