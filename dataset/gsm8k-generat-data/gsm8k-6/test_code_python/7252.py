def solution():
    # Calculate the total cost of gas purchased by Jim
    cost_NC = 10 * 2.00  # cost of 10 gallons of gas in North Carolina
    cost_VA = 10 * (2.00 + 1.00)  # cost of 10 gallons of gas in Virginia, where he paid $1 more per gallon
    total_cost = cost_NC + cost_VA
    result = total_cost
    return result

print(solution())