def solution():
    # Calculate the number of women's T-shirts sold in a week
    women_Tshirts_per_week = ((10*60)/30)*7  # 10 am to 10 pm, 7 days a week

    # Calculate the number of men's T-shirts sold in a week
    men_Tshirts_per_week = ((10*60)/40)*7  # 10 am to 10 pm, 7 days a week

    # Calculate the total earnings per week
    total_earnings_per_week = (women_Tshirts_per_week * 18) + (men_Tshirts_per_week * 15)
    result = total_earnings_per_week
    return result

print(solution())