def solution():
    # Define the number of candies Brent received
    kit_kats = 5
    hershey_kisses = 3 * kit_kats
    nerds = 8
    lollipops = 11
    baby_ruths = 10
    reese_cups = baby_ruths / 2

    # Calculate the total number of candies before giving some to his sister
    total_candies = kit_kats + hershey_kisses + nerds + lollipops + baby_ruths + reese_cups

    # Subtract the number of lollipops Brent gave to his sister
    remaining_candies = total_candies - 5

    result = remaining_candies
    return result

print(solution())