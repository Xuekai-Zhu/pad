def solution():
    # Tanya's total cost
    tanya_face_moisturizer_cost = 50 * 2  # She bought two face moisturizers for $50 each
    tanya_body_lotion_cost = 60 * 4  # She bought four body lotions for $60 each
    tanya_total_cost = tanya_face_moisturizer_cost + tanya_body_lotion_cost

    # Christy's total cost
    christy_total_cost = 2 * tanya_total_cost  # Christy spends twice as much as Tanya

    # Total cost
    total_cost = tanya_total_cost + christy_total_cost
    result = total_cost
    return result

print(solution())