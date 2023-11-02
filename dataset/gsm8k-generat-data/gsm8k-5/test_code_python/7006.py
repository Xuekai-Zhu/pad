def solution():
    num_students = 20  # There are 20 students in Dikembe's class
    floss_per_student = 1.5  # Each student needs 1.5 yards of floss
    total_floss_needed = num_students * floss_per_student  # Total floss needed for all students
    floss_per_packet = 35  # Each packet of floss contains 35 yards
    num_packets_needed = int(total_floss_needed / floss_per_packet) + 1 # Round up and add 1 because we cannot buy a fraction of a packet

    # Calculate the amount of leftover floss
    leftover_floss = (num_packets_needed * floss_per_packet) - total_floss_needed
    result = leftover_floss
    return result

print(solution())