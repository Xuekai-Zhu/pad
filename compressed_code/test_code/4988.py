def solution():
    
    batch_size = 4
    serving_size = 6
    total_people = 42
    batches_needed = total_people / serving_size
    avocados_needed = batches_needed * batch_size
    result = avocados_needed
    return result

print(solution())