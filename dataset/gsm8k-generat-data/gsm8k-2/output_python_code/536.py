def solution():
    """A shipping boat's crew consisted of 17 sailors, with five inexperienced sailors. Each experienced sailor was paid 1/5 times more than the inexperienced sailors. If the inexperienced sailors were paid $10 per hour for a 60-hour workweek, calculate the total combined monthly earnings of the experienced sailors."""
    num_sailors = 17
    num_inexperienced = 5
    inexperienced_pay = 10 * 60  # weekly pay
    experienced_pay = (6 / 5) * inexperienced_pay  # hourly pay for experienced sailors
    num_experienced = num_sailors - num_inexperienced
    total_experienced_pay = num_experienced * experienced_pay * 4  # monthly pay for experienced sailors
    result = total_experienced_pay
    return result

print(solution())