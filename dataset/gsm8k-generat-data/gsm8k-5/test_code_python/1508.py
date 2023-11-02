def solution():
    jemma_price = 5  # Jemma sells glass frames for $5 each
    dorothy_price = jemma_price / 2  # Dorothy sells glass frames at half the price of Jemma

    jemma_quantity = 400  # Jemma sells 400 frames
    dorothy_quantity = jemma_quantity / 2  # Dorothy sells half the quantity of Jemma

    # Calculate the total revenue from Jemma's sales
    jemma_revenue = jemma_price * jemma_quantity

    # Calculate the total revenue from Dorothy's sales
    dorothy_revenue = dorothy_price * dorothy_quantity

    # Calculate the total revenue from both sales combined
    total_revenue = jemma_revenue + dorothy_revenue
    result = total_revenue
    return result

print(solution())