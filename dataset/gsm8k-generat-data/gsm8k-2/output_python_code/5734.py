def solution():
    """Two teams are playing in a stadium with a capacity of 2000 people. The total number of people in the stadium is 3/4 of the total capacity and each person paid $20 in entry fees. What is the difference between the total amount of fees collected when the stadium was 3/4 full and if the stadium would have been full?"""
    capacity = 2000
    total_people = 0.75 * capacity
    full_fee = capacity * 20
    partial_fee = total_people * 20
    difference = full_fee - partial_fee
    result = difference
    return result

print(solution())