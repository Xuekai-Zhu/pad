def solution():
    # Calculate the cost of the wire mesh needed to fence the entire field
    cost_per_foot = 30  # cost of one foot of wire mesh
    total_cost = 120000  # total amount of money available
    total_feet = 5000  # total feet of the field
    fenced_feet = total_feet  # all feet of the field are initially fenced
    while total_cost >= cost_per_foot * fenced_feet:
        total_cost -= cost_per_foot * fenced_feet  # subtract cost of fencing from total cost
        fenced_feet -= 1  # reduce the number of feet being fenced
    unfenced_feet = total_feet - fenced_feet  # calculate the number of feet that are not fenced
    result = unfenced_feet
    return result

print(solution())