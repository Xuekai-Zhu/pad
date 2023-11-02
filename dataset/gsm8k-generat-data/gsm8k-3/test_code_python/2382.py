def solution():
    """Christy and her friend Tanya go to Target to buy some face moisturizer and body lotions. Christy spends twice as much as Tanya, who pays 50$ for two face moisturizers each and 60$ per body lotion, buying four of them. How much money did they spend together in total?"""
    # Define the prices of the face moisturizer and body lotion
    FACE_MOISTURIZER_PRICE = 25  # Two face moisturizers cost 50$
    BODY_LOTION_PRICE = 60

    # Calculate the total amount Tanya spent
    tanya_face_moisturizer_cost = 50
    tanya_body_lotion_cost = 4 * BODY_LOTION_PRICE
    tanya_total_cost = tanya_face_moisturizer_cost + tanya_body_lotion_cost

    # Calculate the total amount Christy spent
    christy_total_cost = 2 * tanya_total_cost

    # Calculate the total amount spent by both of them together
    total_cost = tanya_total_cost + christy_total_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())