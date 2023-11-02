def solution():
    
    starting_jellybeans = 37
    removed_jellybeans = 15
    added_back_jellybeans = 5
    final_removed_jellybeans = 4
    remaining_jellybeans = starting_jellybeans - removed_jellybeans + added_back_jellybeans - final_removed_jellybeans
    result = remaining_jellybeans
    return result

print(solution())