def solution():
    # Calculate the number of balloons remaining after half an hour
    remaining_balloons = 200 * (4/5)  # 1/5 of the total number of balloons have blown up

    # Calculate the number of balloons remaining after another hour
    remaining_balloons -= 2*(1/5)*200  # twice the number of balloons that had already blown up also blow up
    
    result = remaining_balloons
    return result

print(solution())