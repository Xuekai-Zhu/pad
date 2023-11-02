def solution():
    ounces_per_weekday_paper = 8
    ounces_per_sunday_paper = 16
    papers_stolen_per_day = 250
    weeks_not_delivered = 10
    total_papers_not_delivered = papers_stolen_per_day * weeks_not_delivered
    total_ounces_not_delivered = (total_papers_not_delivered * ounces_per_weekday_paper) + (total_papers_not_delivered / 7 * ounces_per_sunday_paper)
    total_pounds_not_delivered = total_ounces_not_delivered / 16
    total_tons_not_delivered = total_pounds_not_delivered / 2000
    recycling_price_per_ton = 20
    total_money_made = total_tons_not_delivered * recycling_price_per_ton
    result = total_money_made
    return result

print(solution())