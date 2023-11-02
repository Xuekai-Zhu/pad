def solution():
    """Charles is wondering how much chocolate milk he can make with all the supplies he finds in the fridge. He is going to keep drinking 8-ounce glasses until he uses up all the ingredients. Each glass must contain 6.5 ounces of milk and 1.5 ounces of chocolate syrup. If he has 130 ounces of milk and 60 ounces of chocolate syrup, how many total ounces ounce of chocolate milk will he drink?"""
    # Calculate the maximum number of glasses of chocolate milk that can be made with the available supplies
    max_glasses = min(130/6.5, 60/1.5)

    # Calculate the total ounces of chocolate milk that can be made
    total_ounces = max_glasses * 8

    # Display the total ounces of chocolate milk that Charles can drink
    result = total_ounces
    return result

print(solution())