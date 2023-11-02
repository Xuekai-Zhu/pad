def solution():
    """Bob has a cube of silver that measures 3 inches on each side. A cubic inch of silver weighs 6 ounces. Each ounce of silver sells for $25. He sells it for 110% of its silver value. How much does he sell it for?"""
    # Define the dimensions of the cube and the weight of one cubic inch of silver
    length = 3
    width = 3
    height = 3
    weight_per_cubic_inch = 6

    # Calculate the total weight of the cube
    total_weight = length * width * height * weight_per_cubic_inch

    # Calculate the value of the silver at $25 per ounce
    silver_value = total_weight * 25

    # Calculate the price he sells it for at 110% of its silver value
    selling_price = silver_value * 1.1

    # Return the result
    result = selling_price
    return result

print(solution())