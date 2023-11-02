def solution():
    # Calculate the total number of candies Brent had
    kitkat_bars = 5
    hershey_kisses = 5 * 3
    nerds_boxes = 8
    lollipops = 11
    baby_ruths = 10
    reese_cups = 10 / 2
    
    total_candies = kitkat_bars + hershey_kisses + nerds_boxes + lollipops + baby_ruths + reese_cups

    # Calculate how many candies Brent had after giving 5 lollipops to his sister
    candies_left = total_candies - 5
    result = candies_left
    return result

print(solution())