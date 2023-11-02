def solution():
    
    file_size = 90
    first_chunk_size = 60
    first_chunk_speed = 5
    second_chunk_speed = 10
    
    first_chunk_time = first_chunk_size / first_chunk_speed
    second_chunk_size = file_size - first_chunk_size
    second_chunk_time = second_chunk_size / second_chunk_speed
    
    total_time = first_chunk_time + second_chunk_time
    result = total_time
    return result

print(solution())