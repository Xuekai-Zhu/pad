def solution():
    
    total_length = 10
    num_parts = 5
    crochet_parts = 3
    length_per_part = total_length / num_parts
    crochet_length = crochet_parts * length_per_part
    result = crochet_length
    return result

print(solution())