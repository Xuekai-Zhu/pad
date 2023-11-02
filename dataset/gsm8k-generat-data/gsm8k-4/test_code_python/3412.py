def solution():
    """Charles is wondering how much chocolate milk he can make with all the supplies he finds in the fridge. He is going to keep drinking 8-ounce glasses until he uses up all the ingredients. Each glass must contain 6.5 ounces of milk and 1.5 ounces of chocolate syrup. If he has 130 ounces of milk and 60 ounces of chocolate syrup, how many total ounces ounce of chocolate milk will he drink?"""
    # Define the amount of milk and chocolate syrup needed per glass
    milk_per_glass = 6.5
    syrup_per_glass = 1.5

    # Calculate the maximum number of glasses he can make with the amount of milk and syrup he has
    max_glasses_milk = 130 / milk_per_glass
    max_glasses_syrup = 60 / syrup_per_glass

    # Take the integer part of the maximum number of glasses to make sure he doesn't exceed the amount of either ingredient
    max_glasses = int(min(max_glasses_milk, max_glasses_syrup))

    # Calculate the total amount of milk and syrup used to make the maximum number of glasses
    milk_used = max_glasses * milk_per_glass
    syrup_used = max_glasses * syrup_per_glass

    # Calculate the total amount of chocolate milk he can make
    total_chocolate_milk = milk_used + syrup_used

    result = total_chocolate_milk
    return result

print(solution())