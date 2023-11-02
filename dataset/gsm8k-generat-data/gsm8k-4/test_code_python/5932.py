def solution():
    """Jenine can sharpen a pencil 5 times before it runs out. She needs to sharpen a pencil for every 1.5 hours of use. She already has ten pencils and needs to write for 105 hours. A new pencil costs $2. How much does she need to spend on more pencils to be able to write for 105 hours?"""
    # Define the number of times a pencil can be sharpened before running out
    SHARPEN_LIMIT = 5
    
    # Define the number of hours a pencil can be used before needing to be sharpened
    PENCIL_LIFE = 1.5
    
    # Define the number of pencils Jenine already has
    current_pencils = 10
    
    # Define the target number of hours Jenine needs to write for
    target_hours = 105
    
    # Calculate the total number of pencils Jenine will need
    total_pencils = ((target_hours / PENCIL_LIFE) * SHARPEN_LIMIT) - current_pencils
    
    # Calculate the cost of buying the additional pencils
    pencil_cost = total_pencils * 2
    
    # return the result
    result = pencil_cost
    return result

print(solution())