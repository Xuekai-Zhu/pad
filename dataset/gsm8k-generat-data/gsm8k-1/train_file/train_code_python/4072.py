def solution():
    """Brogan has two apple trees and goes to harvest them. The first tree is 40% red and 60% green. The second tree is 50% red and 50% green. If they each produce 20 apples, how many red apples does he get?"""
    tree1_red_percentage = 0.4
    tree2_red_percentage = 0.5
    total_apples = 20 + 20
    red_apples = (tree1_red_percentage * 20) + (tree2_red_percentage * 20)
    result = red_apples
    return result

print(solution())