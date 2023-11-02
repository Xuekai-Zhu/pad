def solution():
    """Judy uses 10 pencils during her 5 day school week. A 30 pack of pencils costs $4. How much will she spend on pencils over 45 days?"""
    # Calculate the number of weeks Judy will be in school
    weeks_in_school = 45 / 5

    # Calculate the number of pencils Judy will use over 45 days
    total_pencils = weeks_in_school * 10

    # Calculate the number of pencil packs Judy will need to buy
    total_packs = total_pencils / 30

    # Calculate the total cost of the pencil packs
    total_cost = total_packs * 4

    # Display the total cost
    result = total_cost
    return result

print(solution())