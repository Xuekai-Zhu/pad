def solution():
    """Dikembe wants to teach everyone at school about the importance of flossing, so he plans to bring enough packets of floss for everyone. There are 20 students in his class. Each student needs 1.5 yards of floss. He sees in the store that each packet of floss contains 35 yards. If he buys the least amount necessary, how much floss is left over?"""
    students = 20
    yards_per_student = 1.5
    total_yards = students * yards_per_student
    yards_per_packet = 35
    packets_needed = total_yards / yards_per_packet
    leftover_yards = total_yards - (packets_needed * yards_per_packet)
    result = leftover_yards
    return result

print(solution())