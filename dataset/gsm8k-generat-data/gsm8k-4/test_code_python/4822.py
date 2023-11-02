def solution():
    """James needs to get a new pair of glasses. His frames cost $200 and the lenses cost $500. Insurance will cover 80% of the cost of lenses and he has a $50 off coupon for frames. How much does everything cost?"""
    # Define the cost of frames and lenses
    frame_cost = 200
    lens_cost = 500

    # Define the insurance coverage and coupon discount
    insurance_coverage = 0.8
    coupon_discount = 50

    # Calculate the cost of lenses after insurance coverage
    lenses_after_coverage = lens_cost * (1 - insurance_coverage)

    # Calculate the total cost of the glasses
    total_cost = frame_cost - coupon_discount + lenses_after_coverage

    result = total_cost
    return result

print(solution())