def solution():
    cottage_cost = 5 # cost per hour
    rental_hours = 8
    
    total_cost = cottage_cost * rental_hours # total cost for 8 hours
    
    cost_per_friend = total_cost / 2 # split evenly between two friends
    
    result = cost_per_friend
    return result

print(solution())