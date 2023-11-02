def solution():
    tanya_face_moisturizer_cost = 50/2 # each moisturizer costs 25$
    tanya_num_face_moisturizers = 2
    tanya_num_body_lotions = 4
    tanya_body_lotion_cost = 60
    
    christy_face_moisturizer_cost = tanya_face_moisturizer_cost * 2
    christy_num_face_moisturizers = tanya_num_face_moisturizers
    christy_num_body_lotions = tanya_num_body_lotions
    christy_body_lotion_cost = tanya_body_lotion_cost * 2

    # Calculate the total cost for Tanya
    tanya_total_cost = (tanya_face_moisturizer_cost * tanya_num_face_moisturizers) + (tanya_body_lotion_cost * tanya_num_body_lotions)

    # Calculate the total cost for Christy
    christy_total_cost = (christy_face_moisturizer_cost * christy_num_face_moisturizers) + (christy_body_lotion_cost * christy_num_body_lotions)

    # Calculate the total cost for both of them together
    total_cost = tanya_total_cost + christy_total_cost
    result = total_cost
    return result

print(solution())