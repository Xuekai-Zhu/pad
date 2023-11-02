def solution():
    # Calculate the total amount spent by Andy and Bob
    andy_total = 1 + 2*2  # Andy bought a can of soda at $1 and two hamburgers at $2 each
    bob_total = 2*3 + x  # Bob ordered two sandwiches for $3 and a can of fruit drink whose cost we need to find
    
    # Since they spent the same amount, we can equate their totals and solve for x
    x = andy_total - bob_total + 3
    
    result = x
    return result

print(solution())