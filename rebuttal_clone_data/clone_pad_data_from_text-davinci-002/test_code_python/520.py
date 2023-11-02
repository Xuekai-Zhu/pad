def solution():
    total_layers = 25
    limestone_layers = 5
    sandstone_layers = total_layers - limestone_layers - 4 - ((total_layers - limestone_layers - 4) / 2)
    result = sandstone_layers
    return result

print(solution())