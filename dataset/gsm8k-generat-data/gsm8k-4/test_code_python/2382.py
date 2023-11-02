def solution():
    """Christy and her friend Tanya go to Target to buy some face moisturizer and body lotions. Christy spends twice as much as Tanya, who pays 50$ for two face moisturizers each and 60$ per body lotion, buying four of them. How much money did they spend together in total?"""
    # Define the prices of the face moisturizer and body lotion
    FACE_MOISTURIZER_PRICE = 50 / 2
    BODY_LOTION_PRICE = 60

    # Define the number of items purchased by Tanya
    TANYA_FACE_MOISTURIZERS = 2
    TANYA_BODY_LOTIONS = 4

    # Calculate the total amount spent by Tanya
    tanya_spent = TANYA_FACE_MOISTURIZERS * FACE_MOISTURIZER_PRICE + TANYA_BODY_LOTIONS * BODY_LOTION_PRICE

    # Calculate the amount spent by Christy, who spent double the amount spent by Tanya
    christy_spent = 2 * tanya_spent

    # Calculate the total amount spent by both of them
    total_spent = tanya_spent + christy_spent

    result = total_spent
    return result

print(solution())