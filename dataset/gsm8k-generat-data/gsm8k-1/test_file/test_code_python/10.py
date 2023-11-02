def solution():
    """In a dance class of 20 students, 20% enrolled in contemporary dance, 25% of the remaining enrolled in jazz dance, and the rest enrolled in hip-hop dance. What percentage of the entire students enrolled in hip-hop dance?"""
    total_students = 20
    contemporary_percent = 0.20
    contemporary_students = total_students * contemporary_percent
    remaining_students = total_students - contemporary_students
    jazz_percent = 0.25
    jazz_students = remaining_students * jazz_percent
    hip_hop_students = total_students - contemporary_students - jazz_students
    hip_hop_percent = hip_hop_students / total_students * 100
    result = hip_hop_percent
    return result

print(solution())