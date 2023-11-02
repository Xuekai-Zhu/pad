def solution():
    """Ofelia joined a saving challenge wherein she has to save twice the amount she saved from the previous month. In January, she saved $10. How much is she going to save in May?"""
    # Initialize the amount saved in January and the number of months passed
    saved_amount = 10
    months_passed = 4

    # Calculate the amount saved in May
    for i in range(months_passed):
        saved_amount = saved_amount * 2

    # Return the result
    result = saved_amount
    return result

print(solution())