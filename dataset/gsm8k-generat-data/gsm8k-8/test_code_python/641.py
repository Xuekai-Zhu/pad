def solution():
    # Define the amount of silk needed for one dress and the total amount of silk in storage
    silk_per_dress = 5
    total_silk = 600

    # Calculate the amount of silk given to the friends (5 friends * 20 meters each)
    silk_given_to_friends = 5 * 20

    # Calculate the amount of silk left for Alex
    silk_for_alex = total_silk - silk_given_to_friends

    # Calculate the number of dresses Alex can make
    dresses_to_make = silk_for_alex // silk_per_dress
    result = dresses_to_make
    return result

print(solution())