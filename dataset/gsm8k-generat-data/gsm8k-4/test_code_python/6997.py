def solution():
    """She sold twice as many boxes on Tuesday as she did on Wednesday, and she sold twice as many boxes on Wednesday as she did on Thursday. If Kim sold 1200 boxes of cupcakes on Thursday, how many boxes did she sell on Tuesday?"""
    # Let's start with the number of boxes sold on Thursday
    thursday_sales = 1200

    # Kim sold twice as many boxes on Wednesday as she did on Thursday
    wednesday_sales = 2 * thursday_sales

    # Kim sold twice as many boxes on Tuesday as she did on Wednesday
    tuesday_sales = 2 * wednesday_sales

    # Return the result
    result = tuesday_sales
    return result

print(solution())