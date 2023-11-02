def solution():
    """Dikembe wants to teach everyone at school about the importance of flossing, so he plans to bring enough packets of floss for everyone. There are 20 students in his class. Each student needs 1.5 yards of floss. He sees in the store that each packet of floss contains 35 yards. If he buys the least amount necessary, how much floss is left over?"""
    # Define the number of students and the amount of floss needed per student
    num_students = 20
    floss_per_student = 1.5

    # Calculate the total amount of floss needed
    total_floss_needed = num_students * floss_per_student

    # Calculate the number of floss packets needed
    packets_needed = total_floss_needed / 35
    packets_needed = math.ceil(packets_needed)

    # Calculate the total amount of floss in the packets
    total_floss_in_packets = packets_needed * 35

    # Calculate the amount of floss left over
    floss_left_over = total_floss_in_packets - total_floss_needed

    # return the result
    result = floss_left_over
    return result

print(solution())