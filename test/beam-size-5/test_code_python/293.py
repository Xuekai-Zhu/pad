def solution():
    total_crates = 120  # Sam has a target of 120 crates of bread
    crates_sold_weekend = 20  # Sam sold 20 crates on Monday and Friday
    crates_sold_wednesday = 15  # Sam sold 15 crates on Wednesday
    crates_sold_thursday = 18  # Sam sold 18 crates on Thursday

    # Calculate the total number of crates sold over the week
    total_crates_sold = crates_sold_weekend + crates_sold_wednesday + crates_sold_thursday

    # Calculate the number of crates Sam was off from his target
    crates_off = total_crates - total_crates_sold
    result = crates_off
    return result

print(solution())