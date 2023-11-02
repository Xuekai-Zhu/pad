def solution():
    # Define the number of dogs and minutes for each walk
    dog1 = 1
    dog1_minutes = 10
    dog2 = 2
    dog2_minutes = 7
    dog3 = 3
    dog3_minutes = 9

    # Calculate the total minutes and the total price for each walk
    total_minutes1 = dog1 * dog1_minutes
    total_price1 = 20 * dog1 + total_minutes1

    total_minutes2 = dog2 * dog2_minutes
    total_price2 = 20 * dog2 + total_minutes2

    total_minutes3 = dog3 * dog3_minutes
    total_price3 = 20 * dog3 + total_minutes3

    # Calculate the total earnings
    total_earnings = total_price1 + total_price2 + total_price3
    result = total_earnings
    return result

print(solution())