def solution():
    visit_cost = 300
    cast_cost = 200
    insurance_coverage = 60
    total_cost = visit_cost + cast_cost
    out_of_pocket = total_cost - (insurance_coverage / 100 * total_cost)
    result = out_of_pocket
    return result
 
Question: Sarah takes a long car trip.  She drives an average of 62 miles per hour.  If her trip is 10 hours long, how many total miles does she drive?
Solution:
def solution():
    average_speed = 62
    hours = 10
    total_miles = average_speed * hours
    result = total_miles
    return result

print(solution())