def solution():
    num_students = 20
    floss_per_student = 1.5
    floss_per_packet = 35

    # Calculate the total amount of floss needed
    total_floss_needed = num_students * floss_per_student

    # Calculate the number of packets needed to provide enough floss
    num_packets_needed = (total_floss_needed / floss_per_packet)
    num_packets_needed = round(num_packets_needed + 0.5)  # Round up to ensure enough packets are purchased

    # Calculate the total amount of floss purchased
    total_floss_purchased = num_packets_needed * floss_per_packet

    # Calculate the amount of floss left over
    floss_leftover = total_floss_purchased - total_floss_needed
    result = floss_leftover
    return result

print(solution())