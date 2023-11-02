def solution():
    # Let's call Johnny's current amount of practice "x"
    # As of 20 days ago, he had half as much practice, so his amount of practice 20 days ago was x/2
    # That means in the last 20 days, he has increased his amount of practice by x/2
    # So his current amount of practice is (x + x/2) = 1.5x
    current_practice = 1.5 # We can set this to any value greater than 1 since we don't have an exact amount for x
    days_passed = 0

    # We need to keep increasing the number of days until Johnny has 3 times as much practice as he currently does
    while current_practice < 3:
        # We know that Johnny practices the same amount each day, so we just need to add one day's worth of practice each loop
        current_practice += 1/20
        days_passed += 1

    result = days_passed
    return result

print(solution())