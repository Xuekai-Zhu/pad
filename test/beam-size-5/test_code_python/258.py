def solution():
    
    boxes = 5
    marbles_per_box = 50
    total_marbles = boxes * marbles_per_box
    marbles_received = 20
    remaining_marbles = total_marbles - marbles_received
    result = remaining_marbles
    return result

print(solution())