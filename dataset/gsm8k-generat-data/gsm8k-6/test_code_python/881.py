def solution():
    # Calculate the total amount Mark will spend on theater visits in 6 weeks
    num_performances = 6  # Mark visits the theater once a week for 6 weeks
    price_per_hour = 5  # Price of a theater ticket per hour
    total_hours = 3 * num_performances  # Mark spends 3 hours per visit
    total_cost = price_per_hour * total_hours  
    result = total_cost
    return result

print(solution())