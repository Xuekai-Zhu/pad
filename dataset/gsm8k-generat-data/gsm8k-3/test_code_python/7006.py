def solution():
    """Dikembe wants to teach everyone at school about the importance of flossing, so he plans to bring enough packets of floss for everyone. There are 20 students in his class. Each student needs 1.5 yards of floss. He sees in the store that each packet of floss contains 35 yards. If he buys the least amount necessary, how much floss is left over?"""
    # Calculate the total amount of floss needed for the class
    total_floss_needed = 20 * 1.5 # yards

    # Calculate the number of packets of floss needed
    packets_needed = int(total_floss_needed/35) + 1 # round up to nearest whole packet

    # Calculate the total amount of floss in the packets needed
    total_floss = packets_needed * 35 # yards

    # Calculate the amount of floss left over
    left_over_floss = total_floss - total_floss_needed # yards

    # Display the amount of floss left over
    result = left_over_floss
    return result

print(solution())