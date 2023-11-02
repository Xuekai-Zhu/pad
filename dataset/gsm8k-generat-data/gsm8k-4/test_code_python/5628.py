def solution():
    """Mr. Desmond bought three times as many toys for his younger son as he bought for his elder son. If the elder son received 60 toys, how many toys did Mr Desmond buy?"""
    # Define the number of toys bought for the elder son
    elder_son_toys = 60

    # Calculate the number of toys bought for the younger son
    younger_son_toys = elder_son_toys * 3

    # Calculate the total number of toys bought
    total_toys = elder_son_toys + younger_son_toys

    # return the result
    result = total_toys
    return result

print(solution())