def solution():
    """Bobby buys two packets of candy. He eats two candies every day from Monday through Friday and takes one each during the remaining days of the week. If it takes him 3 such weeks to finish the 2 packets, how many candies are in a packet?"""
    days_per_week = 7
    candies_per_week = 2*5 + 1*2
    candies_per_packet = candies_per_week * 3 / 2
    result = candies_per_packet
    return result

print(solution())