def solution():
    # Define the variables
    first_day = 3
    snails_eaten = first_day
    for i in range(1, 5):
        snails_eaten += first_day + 2*i
    
    result = snails_eaten
    return result

print(solution())