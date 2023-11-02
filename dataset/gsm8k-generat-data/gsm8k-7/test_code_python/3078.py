def solution():
    barbi_loss_per_month = 1.5
    num_months_in_year = 12
    num_years_for_barbi = 1

    luca_loss_per_year = 9
    num_years_for_luca = 11

    # Calculate the total weight loss for Barbi
    total_barbi_loss = barbi_loss_per_month * num_months_in_year * num_years_for_barbi

    # Calculate the total weight loss for Luca
    total_luca_loss = luca_loss_per_year * num_years_for_luca

    # Calculate the difference in weight loss between Luca and Barbi
    difference = total_luca_loss - total_barbi_loss
    result = difference
    return result

print(solution())