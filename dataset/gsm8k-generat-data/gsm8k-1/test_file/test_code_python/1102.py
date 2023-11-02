def solution():
    """Marty has 100 centimeters of ribbon that he must cut into 4 equal parts. Each of the cut parts must be divided into 5 equal parts. How long will each final cut be?"""
    total_length = 100
    num_parts = 4
    length_per_part = total_length / num_parts
    num_subparts = 5
    final_length = length_per_part / num_subparts
    result = final_length
    return result

print(solution())