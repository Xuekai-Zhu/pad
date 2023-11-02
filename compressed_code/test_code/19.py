def solution():
    
    initial_files = 800
    initial_relevant_files = 0.3 * initial_files
    second_download = 400
    second_relevant_files = (2/5) * second_download
    total_relevant_files = initial_relevant_files + second_relevant_files
    result = total_relevant_files
    return result

print(solution())