def solution():
    
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