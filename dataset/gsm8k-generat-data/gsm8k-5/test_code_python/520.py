def solution():
    limestone = 5
    remaining_layers = 25 - limestone
    sandstone = (remaining_layers // 2)
    remaining_layers -= sandstone
    quartz = 4
    remaining_layers -= quartz
    shale = (remaining_layers // 2)
    remaining_layers -= shale
    
    # Calculate the number of layers made of unique kinds of rock
    unique_layers = remaining_layers
    
    result = unique_layers 
    return result

print(solution())