def solution():
    """Two teams are playing in a stadium with a capacity of 2000 people. The total number of people in the stadium is 3/4 of the total capacity and each person paid $20 in entry fees. What is the difference between the total amount of fees collected when the stadium was 3/4 full and if the stadium would have been full?"""
    stadium_capacity = 2000
    people_in_stadium = stadium_capacity * (3/4)
    fee_per_person = 20
    total_fees_75_percent = people_in_stadium * fee_per_person
    total_fees_100_percent = stadium_capacity * fee_per_person
    difference_in_fees = total_fees_100_percent - total_fees_75_percent
    result = difference_in_fees
    return result

print(solution())