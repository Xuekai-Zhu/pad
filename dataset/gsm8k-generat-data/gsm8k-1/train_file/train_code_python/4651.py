def solution():
    """Jamie knows that once she has any more than 32 ounces of liquid she has to use the bathroom, and her teacher said that no one can use the bathroom during the math test. She remembers that she had a cup of milk at lunch and a pint of grape juice at recess. How many ounces can she drink from her water bottle during the test before she'd have to go to the bathroom? (A cup equals 8 ounces and a pint equals 16 ounces.)"""
    max_liquid = 32
    lunch_drink = 8
    recess_drink = 16
    total_drinks = lunch_drink + recess_drink
    remaining_liquid = max_liquid - total_drinks
    result = remaining_liquid
    return result

print(solution())