def solution():
    """Christy and her friend Tanya go to Target to buy some face moisturizer and body lotions. Christy spends twice as much as Tanya, who pays 50$ for two face moisturizers each and 60$ per body lotion, buying four of them. How much money did they spend together in total?"""
    tanya_face_moisturizer_cost = 50 * 2
    tanya_body_lotion_cost = 60 * 4
    tanya_total_cost = tanya_face_moisturizer_cost + tanya_body_lotion_cost
    christy_total_cost = tanya_total_cost * 2
    total_spent = tanya_total_cost + christy_total_cost
    result = total_spent
    return result

print(solution())