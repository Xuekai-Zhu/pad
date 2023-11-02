def solution():
    # Calculate the amount spent by Tanya
    tanya_face_moisturizer_cost = 50  # Tanya pays 50$ for two face moisturizers
    tanya_body_lotion_cost = 60  # Tanya pays 60$ per body lotion, buying 4 of them
    tanya_total_cost = 2 * tanya_face_moisturizer_cost + 4 * tanya_body_lotion_cost

    # Calculate the amount spent by Christy
    christy_total_cost = 2 * tanya_total_cost

    # Calculate the total amount spent by both of them
    total_spent = christy_total_cost + tanya_total_cost
    result = total_spent
    return result

print(solution())