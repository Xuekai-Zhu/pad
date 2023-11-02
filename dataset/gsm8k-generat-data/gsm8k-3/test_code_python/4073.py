def solution():
    """Brogan has two apple trees and goes to harvest them. The first tree is 40% red and 60% green. The second tree is 50% red and 50% green. If they each produce 20 apples, how many red apples does he get?"""
    # Calculate the number of red apples from the first tree
    first_tree_red = 20 * 0.4

    # Calculate the number of red apples from the second tree
    second_tree_red = 20 * 0.5

    # Calculate the total number of red apples
    total_red = first_tree_red + second_tree_red

    # Display the total number of red apples
    result = total_red
    return result

print(solution())