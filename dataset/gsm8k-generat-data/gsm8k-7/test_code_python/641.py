def solution():
    silk_per_dress = 5
    total_silk = 600
    num_friends = 5
    silk_given_to_friends = num_friends * 20

    # Calculate the total amount of silk left for Alex to use
    silk_left = total_silk - silk_given_to_friends

    # Calculate the number of dresses Alex can make
    num_dresses = silk_left // silk_per_dress
    result = num_dresses
    return result

print(solution())