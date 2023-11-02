def solution():
    # Find out how much Dorothy sells each glass frame for
    dorothy_price = 5 / 2

    # Calculate how many frames Dorothy sold
    dorothy_frames = Jemma_frames / 2

    # Calculate how much Jemma made from selling the frames
    jemma_total = Jemma_price * Jemma_frames

    # Calculate how much Dorothy made from selling the frames
    dorothy_total = dorothy_price * dorothy_frames

    # Calculate the total amount made by both of them
    total = jemma_total + dorothy_total

    result = total
    return result

print(solution())