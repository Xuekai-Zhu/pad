def solution():
    kit_kats = 5
    hershey_kisses = 3 * kit_kats
    nerds = 8
    lollipops = 11
    baby_ruths = 10
    reese_cups = baby_ruths / 2
    sister_lollipops = 5

    # Calculate the total number of candies Brent had
    total_candies = kit_kats + hershey_kisses + nerds + lollipops + baby_ruths + reese_cups

    # Subtract the candies given to his sister
    remaining_candies = total_candies - sister_lollipops

    result = remaining_candies
    return result

print(solution())