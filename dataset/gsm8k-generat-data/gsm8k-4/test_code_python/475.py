def solution():
    """Maggie picked 40 apples. Kelsey picked 28 apples. Layla picked some apples, too. The three averaged 30 apples picked. How many did Layla pick?"""
    # Define the number of apples picked by Maggie and Kelsey
    maggie_apples = 40
    kelsey_apples = 28

    # Define the average number of apples picked by the three
    average_apples = 30

    # Calculate the total number of apples picked by the three
    total_apples = (maggie_apples + kelsey_apples + (3 * average_apples)) / 3

    # Calculate the number of apples picked by Layla
    layla_apples = total_apples - maggie_apples - kelsey_apples

    # Return the result
    result = layla_apples
    return result

print(solution())