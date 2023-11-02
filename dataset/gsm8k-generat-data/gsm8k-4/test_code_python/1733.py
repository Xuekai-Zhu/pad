def solution():
    """Adam’s wardrobe is too crowded so he decides to donate some of his clothes to a charity shop. He takes out 4 pairs of pants, 4 jumpers, 4 pajama sets (top and bottom), and 20 t-shirts, then asks his friends if they have anything they want to donate.
    3 of his friends donate the same amount of clothing as Adam each. Then he takes another look over his clothing and decides that he actually wants to keep half of his clothes. How many articles of clothing are being donated in total?"""
    # Calculate the total number of items Adam has initially
    adam_initial = 4 + 4 + (4*2) + 20

    # Calculate the number of items each friend donates
    friend_donation = adam_initial / 3

    # Calculate the total number of items donated by Adam and his friends
    total_donation = (adam_initial + friend_donation*3) / 2

    result = total_donation
    return result

print(solution())