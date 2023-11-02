def solution():
    # Calculate the total number of tadpoles
    num_tadpoles = 3 * 5
    
    # Calculate the number of tadpoles that will survive to maturity
    num_frogs = 2/3 * num_tadpoles
    
    # Calculate the final number of frogs in the pond
    final_num_frogs = 5 + num_frogs
    
    # Calculate the number of frogs that will need to find a new pond
    num_frogs_to_relocate = final_num_frogs - 8
    
    result = num_frogs_to_relocate
    return result

print(solution())