def solution():
    
    initial_files = 800
    percentage_deleted = 70
    remaining_files = initial_files * (100 - percentage_deleted) / 100
    second_round_files = 400
    irrelevant_percentage = 3/5
    relevant_files = second_round_files * (1 - irrelevant_percentage)
    total_valuable_files = remaining_files + relevant_files
    result = total_valuable_files
    return result

print(solution())