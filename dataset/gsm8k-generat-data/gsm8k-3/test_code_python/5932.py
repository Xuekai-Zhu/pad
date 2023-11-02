def solution():
    """Jenine can sharpen a pencil 5 times before it runs out. She needs to sharpen a pencil for every 1.5 hours of use. She already has ten pencils and needs to write for 105 hours. A new pencil costs $2. How much does she need to spend on more pencils to be able to write for 105 hours?"""
    # Define the number of times a pencil can be sharpened and the number of hours per sharpening
    SHARPENINGS = 5
    HOURS_PER_SHARPENING = 1.5

    # Define the number of pencils Jenine has and the number of hours she needs to write
    pencils = 10
    hours_needed = 105

    # Calculate the number of hours each pencil can be used for
    hours_per_pencil = SHARPENINGS * HOURS_PER_SHARPENING

    # Calculate the total number of hours Jenine can write for with her current pencils
    total_hours = (pencils * hours_per_pencil) + (hours_per_pencil * (pencils - 1))

    # Calculate the number of pencils Jenine needs to buy
    pencils_needed = (hours_needed - total_hours) / hours_per_pencil

    # Calculate the cost of the new pencils
    cost = pencils_needed * 2

    # Display the cost of the new pencils
    result = cost
    return result

print(solution())