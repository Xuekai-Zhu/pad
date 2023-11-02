def solution():
    """Alex makes luxury dresses out of silk. Each dress needs 5 meters of silk and Alex has 600 meters of silk in storage. His friends also want to learn how to make these dresses so Alex gives all 5 of them 20 meters of silk each. He uses the rest to make dresses himself. How many dresses can Alex make?"""
    # Define the amount of silk needed per dress
    silk_per_dress = 5

    # Define the total amount of silk in storage
    total_silk = 600

    # Define the amount of silk given to friends
    friend_silk = 5 * 20

    # Calculate the amount of silk left for Alex to use
    alex_silk = total_silk - friend_silk

    # Calculate the number of dresses Alex can make
    num_dresses = alex_silk // silk_per_dress

    # Display the number of dresses Alex can make
    result = num_dresses
    return result

print(solution())