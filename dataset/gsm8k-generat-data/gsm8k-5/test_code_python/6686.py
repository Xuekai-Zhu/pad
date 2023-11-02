def solution():
    guests = 120  # Ashley has 120 wedding guests
    glasses_per_guest = 2  # Ashley wants to serve 2 glasses of champagne to each guest
    servings_per_bottle = 6  # 1 bottle of champagne has 6 servings

    # Calculate the total number of glasses of champagne needed
    total_glasses = guests * glasses_per_guest

    # Calculate the total number of bottles needed, rounding up to the nearest whole number
    total_bottles = math.ceil(total_glasses / servings_per_bottle)

    result = total_bottles
    return result

print(solution())