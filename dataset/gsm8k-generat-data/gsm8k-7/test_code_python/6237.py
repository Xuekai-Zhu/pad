def solution():
    wage_per_hour = 6
    num_8hr_shifts = 2
    num_12hr_shifts = 1
    tip_per_hour = 12
    tax_rate = 0.2  # 20% tax rate
    tip_report_rate = 1/3  # only reports 1/3 of tips to IRS

    # Calculate Brendan's total base earnings from the shifts
    total_base_earnings = (wage_per_hour * ((num_8hr_shifts * 8) + (num_12hr_shifts * 12)))

    # Calculate Brendan's total tips for the week
    total_tips = tip_per_hour * ((num_8hr_shifts + num_12hr_shifts) * 8)

    # Calculate how much of the tips Brendan reports to the IRS
    tips_reported = total_tips * tip_report_rate

    # Calculate Brendan's total earnings for the week
    total_earnings = total_base_earnings + total_tips

    # Calculate Brendan's taxable earnings
    taxable_earnings = total_earnings - tips_reported

    # Calculate Brendan's tax payment for the week
    tax_payment = taxable_earnings * tax_rate
    result = tax_payment
    return result

print(solution())