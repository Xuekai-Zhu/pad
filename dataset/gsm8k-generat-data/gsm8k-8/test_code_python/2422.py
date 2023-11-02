def solution():
    # Calculate the number of fish Bexley brings
    bexley_betta = (2/5) * 10
    bexley_goldfish = (1/3) * 15

    # Calculate the total number of fish before gifting to Hershel's sister
    total_fish = 10 + 15 + bexley_betta + bexley_goldfish

    # Calculate the number of fish gifted to Hershel's sister
    gifted_fish = total_fish / 2

    # Calculate the number of fish remaining in the bowl
    remaining_fish = total_fish - gifted_fish
    result = remaining_fish
    return result

print(solution())