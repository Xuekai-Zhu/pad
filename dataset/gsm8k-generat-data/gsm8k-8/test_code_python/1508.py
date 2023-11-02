def solution():
    # Define Jemma's selling price and number of frames sold
    jemma_price = 5
    jemma_frames = 400

    # Calculate Dorothy's selling price and number of frames sold
    dorothy_price = jemma_price / 2
    dorothy_frames = jemma_frames / 2

    # Calculate the total revenue from Jemma's and Dorothy's sales
    jemma_revenue = jemma_price * jemma_frames
    dorothy_revenue = dorothy_price * dorothy_frames
    total_revenue = jemma_revenue + dorothy_revenue

    result = total_revenue
    return result

print(solution())