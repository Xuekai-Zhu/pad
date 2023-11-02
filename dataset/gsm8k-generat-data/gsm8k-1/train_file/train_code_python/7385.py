def solution():
    """There are 80 passengers on the airplane where the number of men and women is equal. The rest of the passengers are children. How many children are on the airplane if there are 30 men?"""
    total_passengers = 80
    men = 30
    women = total_passengers / 2 - men
    children = total_passengers - men - women
    result = children
    return result

print(solution())