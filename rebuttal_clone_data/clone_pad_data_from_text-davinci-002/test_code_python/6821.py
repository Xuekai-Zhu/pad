def solution():
    work_miles = 6
    work_days = 5
    dog_walks = 2
    dog_days = 7
    friend_house = 1
    friend_visits = 1
    store_miles = 3
    store_visits = 2
    total_miles = (work_miles * work_days) + (dog_walks * dog_days) + (friend_house * friend_visits) + (store_miles * store_visits)
    result = total_miles
    return result

print(solution())