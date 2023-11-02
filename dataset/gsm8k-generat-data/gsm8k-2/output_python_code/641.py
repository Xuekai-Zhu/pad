def solution():
    """Tony has to run several errands in a day. He needs to drive 10 miles to get groceries, 15 miles to get a haircut, and 5 miles to go to a doctor's appointment. How many miles will Tony have driven when he is halfway through driving around for his errands?"""
    total_miles = 10 + 15 + 5
    halfway_miles = total_miles / 2
    miles_driven = 0
    errands = ['groceries', 'haircut', 'doctor']
    for errand in errands:
        if miles_driven + halfway_miles > total_miles // 2:
            break
        if errand == 'groceries':
            miles_driven += 10
        elif errand == 'haircut':
            miles_driven += 15
        elif errand == 'doctor':
            miles_driven += 5

    result = miles_driven
    return result

print(solution())