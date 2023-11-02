def solution():
    """Apple and peach trees are planted in the orchard of the Grange Poser farm. The orchard has 30 apple trees that each give 150 kg of apples and 45 peach trees that each produce an average of 65 kg of fruit. What is the total mass of fruit harvested in this orchard?"""
    # Define the number of apple trees and the yield per tree
    APPLE_TREES = 30
    APPLE_YIELD = 150

    # Define the number of peach trees and the yield per tree
    PEACH_TREES = 45
    PEACH_YIELD = 65

    # Calculate the total yield of apples
    total_apples = APPLE_TREES * APPLE_YIELD

    # Calculate the total yield of peaches
    total_peaches = PEACH_TREES * PEACH_YIELD

    # Calculate the total mass of fruit harvested
    total_fruit = total_apples + total_peaches

    # Display the total mass of fruit
    result = total_fruit
    return result

print(solution())