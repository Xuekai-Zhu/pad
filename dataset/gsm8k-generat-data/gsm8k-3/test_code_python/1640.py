def solution():
    """For Halloween, Taquon, Mack and Jafari put their candy together and they had 418 pieces of candy. If Taquon and Mack each had 171 pieces of candy, how many pieces of candy did Jafari start with?"""
    # Define the total number of pieces of candy
    total_candy = 418

    # Define the number of pieces of candy Taquon and Mack had
    taquon_mack_candy = 171 * 2

    # Calculate the number of pieces of candy Jafari had
    jafari_candy = total_candy - taquon_mack_candy

    # Display the number of pieces of candy Jafari had
    result = jafari_candy
    return result

print(solution())