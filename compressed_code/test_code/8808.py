def solution():
    
    initial_jellybeans = 37
    jellybeans_removed = 15
    jellybeans_added = 5
    jellybeans_removed_again = 4
    total_jellybeans = initial_jellybeans - jellybeans_removed + jellybeans_added - jellybeans_removed_again
    result = total_jellybeans
    return result

print(solution())