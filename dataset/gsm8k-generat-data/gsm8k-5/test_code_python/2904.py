def solution():
    # Calculate the cost of the parts
    parts_cost = 2 * 20  # Mark needed two parts that cost 20 dollars each

    # Calculate the cost of the labor
    labor_cost = (220 - parts_cost)  # Mark spent 220 dollars in total, minus the cost of the parts

    # Calculate the total number of minutes of labor
    labor_minutes = labor_cost / 0.5  # Labor cost is 0.5 dollars per minute

    # Convert labor minutes to labor hours
    labor_hours = labor_minutes / 60  # There are 60 minutes in an hour

    result = labor_hours
    return result

print(solution())