def solution():
    """Adam’s wardrobe is too crowded so he decides to donate some of his clothes to a charity shop. He takes out 4 pairs of pants, 4 jumpers, 4 pajama sets (top and bottom), and 20 t-shirts,
    then asks his friends if they have anything they want to donate. 3 of his friends donate the same amount of clothing as Adam each. Then he takes another look over his clothing and decides that he actually wants to keep half of his clothes. How many articles of clothing are being donated in total?"""
    
    # Calculate the total number of Adam's clothes before donation
    total_clothes = 4 + 4 + (4 * 2) + 20

    # Calculate the total number of clothes donated by Adam's friends
    friends_clothes = total_clothes // 4

    # Calculate the total number of clothes Adam wants to keep
    keep_clothes = total_clothes // 2

    # Calculate the total number of clothes being donated
    donated_clothes = total_clothes - keep_clothes + friends_clothes

    # Display the total number of clothes being donated
    result = donated_clothes
    return result

print(solution())