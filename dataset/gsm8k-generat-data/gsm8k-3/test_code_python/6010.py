def solution():
    """James can do a farmer's walk with 300 pounds per hand for 20 meters.  He can lift 30% more if he only goes 10 meters.  In addition, lifting straps give him another 20%.  How much can he move with lifting straps for 10 meters if he increases his 20-meter distance without straps by 50 pounds and everything else increases in proportion?"""
    # Define the weight and distance for the original farmer's walk
    weight = 300
    distance = 20

    # Calculate the weight for the farmer's walk at 10 meters
    weight_10m = weight + (weight * 0.3)

    # Calculate the weight for the farmer's walk at 20 meters with a 50 pound increase
    weight_20m = weight + 50

    # Calculate the proportion of the weight increase
    weight_proportion = weight_20m / weight

    # Calculate the weight for the farmer's walk at 20 meters with the proportionate weight increase
    weight_20m_prop = weight * weight_proportion

    # Calculate the weight for the farmer's walk at 10 meters with lifting straps
    weight_straps = weight_10m + (weight_10m * 0.2)

    # Display the weight for the farmer's walk at 10 meters with lifting straps
    result = weight_straps
    return result

print(solution())