def solution():
    students = 20
    yards_per_student = 1.5
    total_yards = students * yards_per_student
    yards_per_packet = 35
    packets_bought = total_yards / yards_per_packet
    result = yards_per_packet - (total_yards - (packets_bought * yards_per_packet))
    
    return result

print(solution())