def solution():
    """Quinton is looking to add 4 fruit trees to his backyard.  He wants to plant 2 apple trees that will be 10 feet wide each and need 12 feet between them.  The peach trees will be closer to the house and will grow to be 12 feet wide and will need 15 feet between each tree.  All told, how much space will these trees take up in his yard?"""
    # Define the size and spacing of the apple trees
    APPLE_WIDTH = 10
    APPLE_SPACING = 12

    # Define the size and spacing of the peach trees
    PEACH_WIDTH = 12
    PEACH_SPACING = 15

    # Calculate the total width of the apple trees and their spacing
    apple_width_spacing = (2 * APPLE_WIDTH) + APPLE_SPACING

    # Calculate the total width of the peach trees and their spacing
    peach_width_spacing = (2 * PEACH_WIDTH) + PEACH_SPACING

    # Calculate the total space required for all the trees
    total_space = apple_width_spacing + peach_width_spacing

    # Display the total space required
    result = total_space
    return result

print(solution())