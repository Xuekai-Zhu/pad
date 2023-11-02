def solution():
    """
    Oliver wonders how much water his bathtub can hold. So he takes a bucket that holds 120 ounces and starts filling the bathtub.
    When it reaches the top, he sees that he filled it 14 times. Then he wonders how much bathwater he uses, so he starts taking away
    buckets until it gets to the level he puts it at. He needs to take away 3 buckets to do this. Finally, he wonders how much water he uses
    in a week for his baths, which he takes every day. How much water does he use each week?
    """
    # Define the bucket size and the number of times Oliver filled the bathtub
    bucket_size = 120
    num_fill = 14

    # Calculate the total amount of water used to fill the bathtub
    total_water = bucket_size * num_fill

    # Calculate the amount of water Oliver used for his bath
    bath_water = total_water - (bucket_size * 3)

    # Calculate the amount of water Oliver uses in a week for his daily baths
    weekly_water = bath_water * 7

    result = weekly_water
    return result

print(solution())