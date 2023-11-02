def solution():
    """James needs to get a new pair of glasses.  His frames cost $200 and the lenses cost $500.  Insurance will cover 80% of the cost of lenses and he has a $50 off coupon for frames.  How much does everything cost?"""
    # Define the cost of the frames and lenses
    FRAME_COST = 200
    LENS_COST = 500

    # Apply the coupon to the frame cost
    frame_cost_with_coupon = FRAME_COST - 50

    # Calculate the cost of the lenses after insurance coverage
    lens_cost_after_insurance = LENS_COST * 0.2

    # Calculate the total cost of the glasses
    total_cost = frame_cost_with_coupon + lens_cost_after_insurance

    # Display the total cost
    result = total_cost
    return result

print(solution())