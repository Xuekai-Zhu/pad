def solution():
    
    boxes_of_graham = 14
    packets_of_oreos = 15
    boxes_per_cheesecake = 2
    oreos_per_cheesecake = 3

    cheesecakes_possible = min(boxes_of_graham // boxes_per_cheesecake, packets_of_oreos // oreos_per_cheesecake)
    boxes_of_graham_left = boxes_of_graham - cheesecakes_possible * boxes_per_cheesecake

    result = boxes_of_graham_left
    return result

print(solution())