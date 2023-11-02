def solution():
    cousin_rene = 300
    friend_florence = cousin_rene * 3
    friend_isha = friend_florence / 2
    friend_maria = (cousin_rene + friend_florence + friend_isha) / 3
    total_money = cousin_rene + friend_florence + friend_isha + friend_maria
    result = total_money
    return result

print(solution())