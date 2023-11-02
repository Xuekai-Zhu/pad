def solution():
    """There are 10 6-ounces of glasses that are only 4/5 full of water. How many ounces of water are needed to fill to the brim all those 10 glasses?"""
    # Define the capacity of each glass and the current amount of water in each glass
    glass_capacity = 6
    current_amount = 4/5 * glass_capacity

    # Calculate the amount of water needed to fill each glass
    needed_amount = glass_capacity - current_amount

    # Calculate the total amount of water needed to fill all 10 glasses
    total_amount = needed_amount * 10

    # return the result
    result = total_amount
    return result

print(solution())