def solution():
    """Quinton is looking to add 4 fruit trees to his backyard. He wants to plant 2 apple trees that will be 10 feet wide each and need 12 feet between them. The peach trees will be closer to the house and will grow to be 12 feet wide and will need 15 feet between each tree. All told, how much space will these trees take up in his yard?"""
    # Define the width of the apple trees and the distance between them
    apple_width = 10
    apple_distance = 12

    # Define the width of the peach trees and the distance between them
    peach_width = 12
    peach_distance = 15

    # Calculate the total width of the apple trees
    total_apple_width = (2 * apple_width) + apple_distance

    # Calculate the total width of the peach trees
    total_peach_width = (2 * peach_width) + peach_distance

    # Calculate the total space taken up by all the trees
    total_space = total_apple_width + total_peach_width

    # return the result
    result = total_space
    return result

print(solution())