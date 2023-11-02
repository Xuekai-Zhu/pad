def solution():
    
    starting_count = 180
    friends_count = 40
    brothers_count = 30
    remaining_count = starting_count - friends_count - brothers_count
    sold_count = remaining_count / 2
    final_count = remaining_count - sold_count
    result = final_count
    return result

print(solution())