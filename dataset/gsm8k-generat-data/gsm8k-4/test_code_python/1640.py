def solution():
    """For Halloween, Taquon, Mack and Jafari put their candy together and they had 418 pieces of candy. If Taquon and Mack each had 171 pieces of candy, how many pieces of candy did Jafari start with?"""
    # Define the total number of candy pieces
    total_candy = 418

    # Define the number of candy pieces Taquon and Mack have together
    taquon_mack_candy = 171 * 2

    # Calculate the number of candy pieces Jafari started with
    jafari_candy = total_candy - taquon_mack_candy

    # return the result
    result = jafari_candy
    return result

print(solution())