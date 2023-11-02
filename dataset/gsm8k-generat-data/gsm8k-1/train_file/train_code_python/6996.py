def solution():
    """She sold twice as many boxes on Tuesday as she did on Wednesday, and she sold twice as many boxes on Wednesday as she did on Thursday. If Kim sold 1200 boxes of cupcakes on Thursday, how many boxes did she sell on Tuesday?"""
    thursday_sales = 1200
    wednesday_sales = thursday_sales / 2
    tuesday_sales = wednesday_sales * 2
    result = tuesday_sales
    return result

print(solution())