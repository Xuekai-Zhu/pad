def solution():
    # Calculate the total earnings from stone statues
    stone_earnings = 10 * 20

    # Calculate the total earnings from wooden statues
    wooden_earnings = 20 * 5

    # Calculate the total earnings before taxes
    total_earnings = stone_earnings + wooden_earnings

    # Calculate the amount of taxes to be paid
    taxes = 0.1 * total_earnings

    # Calculate the final earnings after taxes
    final_earnings = total_earnings - taxes

    result = final_earnings
    return result

print(solution())