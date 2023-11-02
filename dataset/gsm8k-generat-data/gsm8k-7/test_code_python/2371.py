def solution():
    tommy_blocks = [(0,0), (0,2), (3,2), (1,2), (1,0)]
    tommy_area = 0
    for i in range(len(tommy_blocks) - 1):
        x1, y1 = tommy_blocks[i]
        x2, y2 = tommy_blocks[i+1]
        tommy_area += abs((x2-x1) * (y2-y1))
        
    friend_area = 80
    result = friend_area / tommy_area
    return result

print(solution())