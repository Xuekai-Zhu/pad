def solution():
    """Bobby buys two packets of candy. He eats two candies every day from Monday through Friday and takes one each during the remaining days of the week. If it takes him 3 such weeks to finish the 2 packets, how many candies are in a packet?"""
    days_per_week = 7
    candies_per_packet = 0
    for i in range(1, 8):
        if i <= 5:  # Monday through Friday
            candies_per_packet += 2
        else:  # Saturday and Sunday
            candies_per_packet += 1
    total_candies_per_week = candies_per_packet * 2  # Bobby eats two packets per week
    total_candies = total_candies_per_week * 3  # It takes him 3 weeks to finish the two packets
    candies_per_packet = total_candies / 2  # Divide total candies by 2 packets to get candies per packet
    result = candies_per_packet
    return result

print(solution())