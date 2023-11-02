def solution():
    """Bobby buys two packets of candy. He eats two candies every day from Monday through Friday and takes one each during the remaining days of the week. If it takes him 3 such weeks to finish the 2 packets, how many candies are in a packet?"""
    # Define the number of days in a week
    days_in_week = 7

    # Define the number of candies eaten each day from Monday to Friday
    candies_per_weekday = 2

    # Define the number of candies eaten each day on the remaining days of the week
    candies_per_weekend = 1

    # Define the number of weeks it takes Bobby to finish the candy
    weeks_to_finish = 3

    # Define the total number of candies in two packets
    total_candies = None

    # Define the number of candies in a single packet
    candies_per_packet = None

    # Calculate the total number of candies Bobby eats in three weeks
    candies_eaten = (candies_per_weekday * 5 + candies_per_weekend * 2) * weeks_to_finish

    # Calculate the total number of candies in two packets
    total_candies = candies_eaten * 2

    # Calculate the number of candies in a single packet
    candies_per_packet = total_candies // 2

    result = candies_per_packet
    return result

print(solution())