def solution():
    """A competition has racers competing on bicycles and tricycles to win a grand prize of $4000. If there are 40 people in the race, and 3/5 of them are riding on bicycles, how many wheels do the bicycles and tricycles in the race have combined?"""
    total_people = 40
    bicycles = round(total_people * 0.6) # 3/5 of 40 people
    tricycles = total_people - bicycles
    bicycle_wheels = bicycles * 2
    tricycle_wheels = tricycles * 3
    total_wheels = bicycle_wheels + tricycle_wheels
    result = total_wheels
    return result

print(solution())