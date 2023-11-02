def solution():
    jemma_price_per_frame = 5
    jemma_sold = 400
    dorothy_sold = jemma_sold / 2
    dorothy_price_per_frame = jemma_price_per_frame / 2
    total_revenue = (dorothy_sold * dorothy_price_per_frame) + (jemma_sold * jemma_price_per_frame)
    result = total_revenue
    
    return result

print(solution())