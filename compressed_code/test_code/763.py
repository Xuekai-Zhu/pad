def solution():
    
    woodblocks_per_log = 5
    total_woodblocks = 80
    available_logs = 8
    woodblocks_from_available_logs = available_logs * woodblocks_per_log
    remaining_woodblocks = total_woodblocks - woodblocks_from_available_logs
    additional_logs_needed = (remaining_woodblocks + woodblocks_per_log - 1) // woodblocks_per_log
    result = additional_logs_needed
    return result

print(solution())