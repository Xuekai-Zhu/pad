def solution():
    """Wendy has 5 facial products she puts on in the morning and she waits 5 minutes between each product.
    She also spends an additional 30 minutes putting on her make-up. How much time does it take her to put on her "full face?" """
    # Calculate the time it takes to apply facial products
    time_products = 5 * 5  # 5 minutes for each product

    # Calculate the total time to put on make-up
    total_time = time_products + 30

    result = total_time
    return result

print(solution())