def solution():
    """Wendy has 5 facial products she puts on in the morning and she waits 5 minutes between each product. She also spends an additional 30 minutes putting on her make-up. How much time does it take her to put on her "full face?" """
    # Define the number of facial products and the time spent waiting between each product
    num_products = 5
    wait_time = 5

    # Calculate the time spent applying facial products
    product_time = num_products * wait_time

    # Add the time spent applying makeup
    total_time = product_time + 30

    # return the result
    result = total_time
    return result

print(solution())