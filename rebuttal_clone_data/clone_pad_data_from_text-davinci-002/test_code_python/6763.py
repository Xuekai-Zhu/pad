def solution(stan_boxes):
     stan_boxes = 100
     joseph_boxes = stan_boxes * 0.2
     jules_boxes = joseph_boxes + 5
     john_boxes = jules_boxes + (jules_boxes * 0.2)
     result = john_boxes
     return result

print(solution())