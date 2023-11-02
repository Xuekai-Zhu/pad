def solution():
    grocery_store = 8
    school = 6
    soccer_practice = 12
    home_again = school + soccer_practice
    total_distance = grocery_store + school + soccer_practice + home_again
    mpg = 25
    gas_cost = 2.50
    gallons_used = total_distance / mpg
    total_cost = gas_cost * gallons_used
    result = total_cost
    return result

print(solution())