def solution():
    
    tanya_face_moisturizer_cost = 50
    tanya_body_lotion_cost = 60
    tanya_total_cost = (tanya_face_moisturizer_cost * 2) + (tanya_body_lotion_cost * 4)
    christy_total_cost = tanya_total_cost * 2
    total_cost = tanya_total_cost + christy_total_cost
    result = total_cost
    return result

print(solution())