def solution():
    cherry_sweets = 30
    strawberry_sweets = 40
    pineapple_sweets = 50

    # Calculate the number of cherry sweets that Aaron eats
    eaten_cherry_sweets = cherry_sweets / 2

    # Calculate the number of strawberry sweets that Aaron eats
    eaten_strawberry_sweets = strawberry_sweets / 2

    # Calculate the number of pineapple sweets that Aaron eats
    eaten_pineapple_sweets = pineapple_sweets / 2

    # Calculate the total number of sweets that Aaron eats
    total_eaten_sweets = eaten_cherry_sweets + eaten_strawberry_sweets + eaten_pineapple_sweets

    # Subtract the number of sweets Aaron eats and gives away from the total number of sweets
    remaining_sweets = (cherry_sweets + strawberry_sweets + pineapple_sweets) / 2 - total_eaten_sweets - 5
    result = remaining_sweets
    return result

print(solution())