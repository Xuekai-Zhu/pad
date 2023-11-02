def solution():
    # Calculate time spent waiting between facial products
    wait_time = 5 * 4  # Wendy waits 5 minutes between each of the 4 products after the first

    # Calculate total time spent on facial products
    product_time = 5 + wait_time  # Wendy spends 5 minutes on the first product and an additional 20 minutes waiting

    # Add time spent on make-up
    total_time = product_time + 30  # Wendy spends an additional 30 minutes putting on make-up

    result = total_time
    return result

print(solution())