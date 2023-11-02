def solution():
    total_boxes = 10
    total_friends = 5
    pencils_left = total_boxes * (10 - 1) # Arnel kept 10 pencils for himself, so each box has 10-1=9 pencils left
    total_pencils_shared = pencils_left // total_friends # divide pencils equally among friends
    pencils_in_each_box = total_pencils_shared + 10 # add the 10 pencils Arnel kept to find the total pencils in each box
    result = pencils_in_each_box
    return result

print(solution())