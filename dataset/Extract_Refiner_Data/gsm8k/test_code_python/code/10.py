def solution():
    
    total_students = 20
    contemporary_dance_students = total_students * 0.2
    remaining_students = total_students - contemporary_dance_students
    jazz_dance_students = remaining_students * 0.25
    hip_hop_dance_students = total_students - contemporary_dance_students - jazz_dance_students
    hip_hop_dance_percentage = (hip_hop_dance_students / total_students) * 100
    result = hip_hop_dance_percentage
    return result

print(solution())