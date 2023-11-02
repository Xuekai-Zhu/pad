def solution():
    pyramid = [64]
    for _ in range(4):
        new_layer = int(pyramid[-1] * 0.8)
        pyramid.append(new_layer)
    
    result = sum(pyramid)
    return result

print(solution())