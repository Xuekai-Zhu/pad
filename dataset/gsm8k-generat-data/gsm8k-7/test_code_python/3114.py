def solution():
    goal = 150
    sold_so_far = 5 + 20 + 10 + 30 + 10 # 5 from first customer, 20 from second, 10 from third, 30 from fourth, 10 from last
    boxes_left = goal - sold_so_far
    result = boxes_left
    return result

print(solution())