def solution():
    # Calculate how much Tom paid in insurance premiums
    insurance_cost = 20 * 24

    # Calculate how much the insurance covers
    insurance_coverage = 0.8 * 5000

    # Calculate how much Tom has to pay out of pocket
    out_of_pocket = 5000 - insurance_coverage

    # Calculate how much money Tom saved by having insurance
    saved_by_insurance = insurance_coverage - insurance_cost

    result = saved_by_insurance
    return result

print(solution())