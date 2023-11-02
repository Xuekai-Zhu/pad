def solution():    
    # Calculate the total number of feathers in the goose
    total_feathers = 3600
    
    # Calculate the number of pounds of feathers in the goose
    pounds_of_feathers = total_feathers / 300
    
    # Calculate the number of pillows Miranda can stuff with the goose's feathers
    number_of_pillows = pounds_of_feathers / 2
    
    result = int(number_of_pillows)  # round down to the nearest integer
    return result

print(solution())