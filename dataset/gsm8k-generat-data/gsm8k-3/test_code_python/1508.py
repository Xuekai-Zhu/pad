def solution():
    """Dorothy sells glass frames at half the price that Jemma sells them. Jemma sells the glass frames at 5 dollars each, selling twice as many frames as Dorothy does. If Jemma sold 400 frames, how much did they make together in total from the sale of the glass frames?"""
    # Define the price of the glass frames sold by Jemma
    jemma_price = 5

    # Define the number of frames sold by Jemma
    jemma_frames = 400

    # Calculate the price of the glass frames sold by Dorothy
    dorothy_price = jemma_price / 2

    # Calculate the number of frames sold by Dorothy
    dorothy_frames = jemma_frames / 2

    # Calculate the total revenue made by Jemma and Dorothy together
    total_revenue = jemma_price * jemma_frames + dorothy_price * dorothy_frames

    # Display the total revenue
    result = total_revenue
    return result

print(solution())