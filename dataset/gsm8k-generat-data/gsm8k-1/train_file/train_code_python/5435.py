def solution():
    """Wendy has 5 facial products she puts on in the morning and she waits 5 minutes between each product. She also spends an additional 30 minutes putting on her make-up. How much time does it take her to put on her "full face?" """
    num_products = 5
    time_between_products = 5
    makeup_time = 30
    total_time = (num_products - 1) * time_between_products + makeup_time
    result = total_time
    return result

print(solution())