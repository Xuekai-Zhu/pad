def solution():
    frame_cost = 200  # Cost of the frames is $200
    lens_cost = 500  # Cost of the lenses is $500

    # Calculate the cost of the lenses after insurance coverage
    lens_cost_after_insurance = lens_cost * 0.2  # Insurance covers 80% of lens cost
    lens_cost_with_insurance = lens_cost - lens_cost_after_insurance

    # Calculate the total cost with coupon and insurance
    total_cost = frame_cost + lens_cost_with_insurance - 50  # $50 off with coupon
    result = total_cost
    return result

print(solution())