def solution():
    
    pepper_time = 3
    onion_time = 4
    cheese_time = 1
    assemble_time = 5
    num_omelets = 5
    num_peppers = 4
    num_onions = 2
    total_pepper_time = num_peppers * pepper_time
    total_onion_time = num_onions * onion_time
    total_cheese_time = num_omelets * cheese_time
    total_assemble_time = num_omelets * assemble_time
    total_time = total_pepper_time + total_onion_time + total_cheese_time + total_assemble_time
    result = total_time
    return result

print(solution())