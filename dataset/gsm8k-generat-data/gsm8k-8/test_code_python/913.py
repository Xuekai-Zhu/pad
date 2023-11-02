def solution():

    # Get profit and donation amounts
    profit = 960
    donation = 310

    # Split profit in half
    profit_half = profit / 2

    # Add donation to half of profit
    total_money = profit_half + donation

    # Calculate the amount she earned above her goal
    extra_money = total_money - 610
    result = extra_money
    return result

print(solution())