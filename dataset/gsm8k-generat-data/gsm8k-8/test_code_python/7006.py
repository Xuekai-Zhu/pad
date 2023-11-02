def solution():
    # Calculate the total amount of floss needed
    total_floss_needed = 20 * 1.5

    # Calculate the number of packets needed
    packets_needed = (total_floss_needed // 35) + 1

    # Calculate the total amount of floss in the packets
    total_floss_in_packets = packets_needed * 35

    # Calculate the amount of leftover floss
    leftover_floss = total_floss_in_packets - total_floss_needed
    result = leftover_floss
    return result

print(solution())