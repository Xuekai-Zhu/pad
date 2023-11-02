def solution():
    """Brogan has two apple trees and goes to harvest them. The first tree is 40% red and 60% green. The second tree is 50% red and 50% green. If they each produce 20 apples, how many red apples does he get?"""
    # Define the number of apples produced by each tree
    tree1_apples = 20
    tree2_apples = 20

    # Calculate the number of red apples from the first tree
    tree1_red_apples = tree1_apples * 0.4

    # Calculate the number of red apples from the second tree
    tree2_red_apples = tree2_apples * 0.5

    # Calculate the total number of red apples
    total_red_apples = tree1_red_apples + tree2_red_apples

    # Return the result
    result = total_red_apples
    return result

print(solution())