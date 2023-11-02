def solution():
    """Ofelia joined a saving challenge wherein she has to save twice the amount she saved from the previous month. In January, she saved $10. How much is she going to save in May?"""
    start_amount = 10
    target_month = 5
    current_amount = start_amount
    for i in range(2, target_month + 1):
        current_amount *= 2

    result = current_amount
    return result

print(solution())