def solution():
    weight_of_white_rhino = 5100    # in pounds
    weight_of_black_rhino = 2000   # in pounds
    num_white_rhinos = 7
    num_black_rhinos = 8
 
    # Calculate the total weight of all the white rhinos
    total_weight_of_white_rhinos = weight_of_white_rhino * num_white_rhinos
  
    # Calculate the total weight of all the black rhinos
    total_weight_of_black_rhinos = weight_of_black_rhino * num_black_rhinos

    # Calculate the total weight of all the rhinos
    total_weight_of_rhinos = total_weight_of_white_rhinos + total_weight_of_black_rhinos
    result = total_weight_of_rhinos
    return result

print(solution())