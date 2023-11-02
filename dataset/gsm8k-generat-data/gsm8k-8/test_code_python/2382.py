def solution():
    # Calculate the total cost of Tanya's purchases
    face_moisturizer_cost = 50 * 2
    body_lotion_cost = 60 * 4
    tanya_total_cost = face_moisturizer_cost + body_lotion_cost

    # Calculate Christy's total cost
    christy_total_cost = tanya_total_cost * 2

    # Calculate the total cost of their purchases
    total_cost = christy_total_cost + tanya_total_cost
    result = total_cost
    return result

print(solution())