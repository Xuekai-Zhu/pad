def solution():
    
    initial_elephants = 30000
    exodus_rate = 2880
    exodus_time = 4
    remaining_elephants = initial_elephants - (exodus_rate * exodus_time)
    final_elephants = 28980
    entering_elephants = (final_elephants - remaining_elephants) / 7
    result = entering_elephants
    return result

print(solution())