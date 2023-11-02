def solution():
    # Let d be the distance between station A and B
    # Let s be the speed of the car
    # Then the speed of the train is s - r, where r is the speed ratio
    # We have s = d/4.5 and r = d/(2+2/3) - s = d/7.5 - d/4.5 = (2d/45)
    # Hence the speed of the train is (2d/45), and the time it takes is d/(2d/45) = 22.5 hours
    # The car takes 4.5 hours, so the total time is 22.5+4.5 = 27 hours

    time_train = 22.5
    time_car = 4.5

    total_time = time_train + time_car
    result = total_time
    return result

print(solution())