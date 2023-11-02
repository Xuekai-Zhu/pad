def solution():
    # Calculate the total number of colored pencils
    total_pencils = 150 + 30  # Eric sorted 150 pencils and another teacher brought 30 more
    evenly_distributed_pencils = total_pencils // 5  # Divide the pencils evenly among 5 containers
    result = evenly_distributed_pencils
    return result

print(solution())