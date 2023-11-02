def solution():
    """Adam’s wardrobe is too crowded so he decides to donate some of his clothes to a charity shop. He takes out 4 pairs of pants, 4 jumpers, 4 pajama sets (top and bottom), and 20 t-shirts, then asks his friends if they have anything they want to donate. 3 of his friends donate the same amount of clothing as Adam each. Then he takes another look over his clothing and decides that he actually wants to keep half of his clothes. How many articles of clothing are being donated in total?"""
    initial_count = 4 + 4 + (4 * 2) + 20
    friend_count = initial_count / 4
    total_count = (initial_count + (friend_count * initial_count)) / 2
    donated_count = initial_count - (total_count / 2)
    result = donated_count
    return result

print(solution())