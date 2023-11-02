def solution():
    # Define the number of people on bicycles and tricycles
    num_bicycles = 3/5 * 40
    num_tricycles = 40 - num_bicycles

    # Calculate the number of wheels on the bicycles and tricycles
    total_wheels = num_bicycles*2 + num_tricycles*3
    result = total_wheels
    return result

print(solution())