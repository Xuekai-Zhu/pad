def solution():
    # Calculate the total number of candies eaten in 3 weeks
    total_candies_eaten = (2*5*3) + (1*2*4*3)  # 2 candies eaten from Monday to Friday, and 1 candy eaten on other days, for 3 weeks

    # Calculate the total number of candies in 2 packets
    total_candies = total_candies_eaten + (2*3)  # 2 candies are left in each packet after 3 weeks

    # Calculate the number of candies in one packet
    candies_per_packet = total_candies / 2

    result = candies_per_packet
    return result

print(solution())