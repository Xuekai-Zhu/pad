def solution():
    """Elsie has a specific amount of wet wipes in a container in the morning. Throughout the day, she refills the container with 10 more wipes after using up 20. By nighttime, she only has 60 wipes left. How many wipes were in the container in the morning?"""
    refill_amount = 10
    usage_amount = 20
    remaining_amount = 60
    total_refills = (remaining_amount - usage_amount) / (refill_amount - usage_amount)
    initial_amount = remaining_amount + total_refills * refill_amount
    result = initial_amount
    return result

print(solution())