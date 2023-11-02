def solution():
    
    total_layers = 25
    limestone_layers = 5
    remaining_layers = total_layers - limestone_layers
    sandstone_layers = remaining_layers // 2
    remaining_layers -= sandstone_layers
    quartz_layers = 4
    remaining_layers -= quartz_layers
    shale_layers = remaining_layers // 2
    one_layer_rocks = remaining_layers - shale_layers
    result = one_layer_rocks
    return result

print(solution())