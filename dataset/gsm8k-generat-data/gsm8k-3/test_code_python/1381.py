def solution():
    """Oliver wonders how much water his bathtub can hold. So he takes a bucket that holds 120 ounces and starts filling the bathtub. When it reaches the top, he sees that he filled it 14 times. Then he wonders how much bathwater he uses, so he starts taking away buckets until it gets to the level he puts it at. He needs to take away 3 buckets to do this. Finally, he wonders how much water he uses in a week for his baths, which he takes every day. How much water does he use each week?"""
    # Define the size of Oliver's bucket in ounces
    BUCKET_SIZE = 120

    # Calculate the total amount of water in the bathtub
    bathtub_water = BUCKET_SIZE * 14

    # Take away 3 buckets to get the desired water level
    bathtub_water -= BUCKET_SIZE * 3

    # Calculate the amount of water Oliver uses for a single bath
    bath_water = bathtub_water / 14

    # Calculate the amount of water Oliver uses each week for his daily baths
    weekly_water = bath_water * 7

    # Display the amount of water Oliver uses each week
    result = weekly_water
    return result

print(solution())