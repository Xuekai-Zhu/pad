def solution():
    """Jamie knows that once she has any more than 32 ounces of liquid she has to use the bathroom, and her teacher said that no one can use the bathroom during the math test. She remembers that she had a cup of milk at lunch and a pint of grape juice at recess. How many ounces can she drink from her water bottle during the test before she'd have to go to the bathroom? (A cup equals 8 ounces and a pint equals 16 ounces.)"""
    # Calculate the total ounces of liquid Jamie has already consumed
    lunch_drink = 8  # Jamie had a cup of milk at lunch
    recess_drink = 16  # Jamie had a pint of grape juice at recess
    total_consumed = lunch_drink + recess_drink

    # Calculate the maximum amount of water Jamie can drink before needing to use the bathroom
    max_allowed = 32 - total_consumed

    # Display the maximum amount of water Jamie can drink
    result = max_allowed
    return result

print(solution())