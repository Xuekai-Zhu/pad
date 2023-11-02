def solution():
    """Dorothy sells glass frames at half the price that Jemma sells them. Jemma sells the glass frames at 5 dollars each, selling twice as many frames as Dorothy does. If Jemma sold 400 frames, how much did they make together in total from the sale of the glass frames?"""
    jemma_price = 5
    dorothy_price = jemma_price / 2
    dorothy_frames = 400 / 2
    jemma_frames = 400
    total_sales = jemma_frames * jemma_price + dorothy_frames * dorothy_price
    result = total_sales
    return result

print(solution())