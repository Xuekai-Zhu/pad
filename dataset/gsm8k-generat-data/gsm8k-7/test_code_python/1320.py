def solution():
    haircuts = 8
    haircut_pay = 12

    styles = 5
    style_pay = 25

    # Calculate the total amount earned from haircuts
    total_haircut_earnings = haircuts * haircut_pay

    # Calculate the total amount earned from styles
    total_style_earnings = styles * style_pay

    # Calculate the total amount earned
    total_earnings = total_haircut_earnings + total_style_earnings
    result = total_earnings
    return result

print(solution())