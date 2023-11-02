def solution():
    """Dorothy sells glass frames at half the price that Jemma sells them. Jemma sells the glass frames at 5 dollars each, selling twice as many frames as Dorothy does. If Jemma sold 400 frames, how much did they make together in total from the sale of the glass frames?"""
    # Define the price of glass frames sold by Jemma and the number of frames she sold
    jemma_price = 5
    jemma_frames = 400

    # Calculate the number of frames sold by Dorothy
    dorothy_frames = jemma_frames / 2

    # Calculate the price of glass frames sold by Dorothy
    dorothy_price = jemma_price / 2

    # Calculate the total amount made by both sellers
    total_amount = jemma_price * jemma_frames + dorothy_price * dorothy_frames

    # Return the result
    result = total_amount
    return result

print(solution())