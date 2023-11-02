def solution():
    
    sandwiches_made = 12
    sandwiches_first_day = sandwiches_made / 2
    sandwiches_second_day = sandwiches_first_day - 2
    sandwiches_left = sandwiches_made - sandwiches_first_day - sandwiches_second_day
    result = sandwiches_left
    
    return result

print(solution())