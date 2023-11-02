def solution():
    # Calculate the total yards of floss needed
    total_yards = 20 * 1.5 

    # Calculate the number of packets needed, rounding up to ensure enough
    packets_needed = math.ceil(total_yards / 35)

    # Calculate the total yards of floss in the packets
    total_floss = packets_needed * 35

    # Calculate the amount of floss left over
    leftover_floss = total_floss - total_yards

    result = leftover_floss
    return result

print(solution())