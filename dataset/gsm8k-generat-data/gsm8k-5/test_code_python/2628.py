def solution():
    # Calculate total money John receives from grandparents
    total_money = 50 * 4  # 50 dollars from each of the 4 grandparents

    # Calculate number of birds John can buy
    num_birds = total_money / 20  # Each bird costs $20

    # Calculate total number of wings using the number of birds
    total_wings = num_birds * 2  # Each bird has 2 wings

    result = total_wings
    return result

print(solution())