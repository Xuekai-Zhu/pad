def solution():
    """Tim's cat bit him. He decided to get himself
    and the cat checked out. His doctor's visits $300
    and insurance covered 75%. His cat's visit cost $120
    and his pet insurance covered $60. How much did he pay?"""
    # Calculate Tim's out-of-pocket cost for his doctor's visit
    tim_doctor_cost = 300 * (1 - 0.75)

    # Calculate Tim's out-of-pocket cost for his cat's visit
    tim_cat_cost = 120 - 60

    # Add Tim's out-of-pocket costs for both visits
    total_cost = tim_doctor_cost + tim_cat_cost

    result = total_cost
    return result

print(solution())