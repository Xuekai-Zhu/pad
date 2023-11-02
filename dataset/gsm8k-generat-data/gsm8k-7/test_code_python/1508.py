def solution():
    jemma_price = 5
    jemma_num_frames = 400
    dorothy_num_frames = jemma_num_frames / 2  # Dorothy sells half the amount Jemma sells
    dorothy_price = jemma_price / 2  # Dorothy sells at half the price Jemma sells

    # Calculate Jemma's total sales
    jemma_sales = jemma_num_frames * jemma_price

    # Calculate Dorothy's total sales
    dorothy_sales = dorothy_num_frames * dorothy_price

    # Calculate the total sales for both Jemma and Dorothy
    total_sales = jemma_sales + dorothy_sales
    result = total_sales
    return result

print(solution())