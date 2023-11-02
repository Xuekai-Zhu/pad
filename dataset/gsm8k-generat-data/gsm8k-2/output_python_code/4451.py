def solution():
    """There are one-third as many Ford trucks as Dodge trucks in the parking lot of the Taco Castle. But there are twice as many Ford trucks as Toyota trucks in this parking lot, and there are half as many Volkswagen Bugs as there are Toyota trucks in this same parking lot. If there are 5 Volkswagon Bugs in the parking lot, how many Dodge trucks are in the parking lot of the Taco Castle?"""
    vw_bugs = 5
    toyota_trucks = vw_bugs * 2
    ford_trucks = toyota_trucks * 2
    dodge_trucks = ford_trucks * 3
    result = dodge_trucks
    return result

print(solution())