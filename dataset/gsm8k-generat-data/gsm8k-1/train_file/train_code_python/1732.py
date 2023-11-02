def solution():
    """Adam’s wardrobe is too crowded so he decides to donate some of his clothes to a charity shop. He takes out 4 pairs of pants, 4 jumpers, 4 pajama sets (top and bottom), and 20 t-shirts, then asks his friends if they have anything they want to donate. 3 of his friends donate the same amount of clothing as Adam each. Then he takes another look over his clothing and decides that he actually wants to keep half of his clothes. How many articles of clothing are being donated in total?"""
    adam_pants = 4
    adam_jumpers = 4
    adam_pajama_sets = 4
    adam_t_shirts = 20
    adam_total_clothing = adam_pants + adam_jumpers + adam_pajama_sets + adam_t_shirts
    
    friends_donation = adam_total_clothing
    total_donation = (adam_total_clothing + friends_donation * 3) / 2
    
    result = total_donation
    return result

print(solution())