def solution():
    """Bobby buys two packets of candy. He eats two candies every day from Monday through Friday and takes one each during the remaining days of the week. If it takes him 3 such weeks to finish the 2 packets, how many candies are in a packet?"""
    # Define the total number of days Bobby eats candies per week
    WEEKDAY_DAYS = 5
    WEEKEND_DAYS = 2
    WEEKDAY_EATEN = 2
    WEEKEND_EATEN = 1

    # Define the total number of weeks it takes Bobby to finish the candy packets
    NUM_WEEKS = 3

    # Calculate the total number of candies eaten by Bobby over the three weeks
    weekday_candies = WEEKDAY_DAYS * WEEKDAY_EATEN
    weekend_candies = WEEKEND_DAYS * WEEKEND_EATEN
    total_candies = (weekday_candies + weekend_candies) * NUM_WEEKS * 2

    # Calculate the number of candies in each packet
    candies_per_packet = total_candies / 2

    # Display the number of candies in each packet
    result = candies_per_packet
    return result

print(solution())