def solution():
    
    jemma_price = 5
    dorothy_price = jemma_price / 2
    dorothy_frames = 400 / 2
    jemma_frames = 400
    total_sales = jemma_frames * jemma_price + dorothy_frames * dorothy_price
    result = total_sales
    return result

print(solution())