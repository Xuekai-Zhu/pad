def solution():
    cost_of_EpiPen = 500  # Cost of one EpiPen
    insurance_coverage = 0.75  # Insurance covers 75% of the cost
    num_EpiPens_per_year = 2  # John gets a new EpiPen every 6 months, so 2 per year

    # Calculate the total cost of EpiPens per year
    total_cost_per_year = cost_of_EpiPen * num_EpiPens_per_year

    # Calculate the amount covered by insurance
    insurance_payment = total_cost_per_year * insurance_coverage

    # Calculate the amount John pays out of pocket per year
    out_of_pocket_payment = total_cost_per_year - insurance_payment

    result = out_of_pocket_payment
    return result

print(solution())