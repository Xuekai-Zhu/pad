def solution():
    giraffe_height = 20 #in feet
    giraffe_neck_length = 7 #in feet
    total_giraffe_height = giraffe_height + giraffe_neck_length
    eiffel_tower_height = 1063 #in feet
    if total_giraffe_height > eiffel_tower_height:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())