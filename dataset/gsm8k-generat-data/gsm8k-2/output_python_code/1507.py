def solution():
    """Dorothy sells glass frames at half the price that Jemma sells them. Jemma sells the glass frames at 5 dollars each, selling twice as many frames as Dorothy does. If Jemma sold 400 frames, how much did they make together in total from the sale of the glass frames?"""
    jemma_price = 5
    jemma_frames = 400
    dorothy_frames = jemma_frames / 2
    dorothy_price = jemma_price / 2
    jemma_earnings = jemma_price * jemma_frames
    dorothy_earnings = dorothy_price * dorothy_frames
    total_earnings = jemma_earnings + dorothy_earnings
    result = total_earnings
    return result

print(solution())