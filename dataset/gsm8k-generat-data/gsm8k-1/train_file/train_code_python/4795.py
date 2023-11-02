def solution():
    """In a yard, the number of tanks is five times the number of trucks. If there are 20 trucks in the yard, calculate the total number of tanks and trucks in the yard."""
    trucks = 20
    tanks = trucks * 5
    total = trucks + tanks
    result = (trucks, tanks, total)
    return result

print(solution())