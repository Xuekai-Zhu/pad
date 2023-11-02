def solution():
    normal_haircuts = 5
    special_haircuts = 3
    trendy_haircuts = 2
    normal_haircut_price = 5
    special_haircut_price = 6
    trendy_haircut_price = 8
    days_per_week = 7

    # Calculate the total earnings from normal haircuts
    normal_haircut_earnings = normal_haircuts * normal_haircut_price * days_per_week

    # Calculate the total earnings from special haircuts
    special_haircut_earnings = special_haircuts * special_haircut_price * days_per_week

    # Calculate the total earnings from trendy haircuts
    trendy_haircut_earnings = trendy_haircuts * trendy_haircut_price * days_per_week

    # Calculate the total earnings for the week
    total_earnings = normal_haircut_earnings + special_haircut_earnings + trendy_haircut_earnings

    result = total_earnings
    return result

print(solution())