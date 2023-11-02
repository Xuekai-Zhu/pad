def solution():
    """Paul is at a train station and is waiting for his train. He isn't sure how long he needs to wait, but he knows that the fourth train scheduled to arrive at the station is the one he needs to get on. The first train is scheduled to arrive in 10 minutes, and this train will stay in the station for 20 minutes. The second train is to arrive half an hour after the first train leaves the station, and this second train will stay in the station for a quarter of the amount of time that the first train stayed in the station. The third train is to arrive an hour after the second train leaves the station, and this third train is to leave the station immediately after it arrives. The fourth train will arrive 20 minutes after the third train leaves, and this is the train Paul will board. In total, how long, in minutes, will Paul wait for his train?"""
    train1_arrival = 10
    train1_stay = 20
    train2_arrival = train1_arrival + 30
    train2_stay = train1_stay / 4
    train3_arrival = train2_arrival + 60
    train3_stay = 0
    train4_arrival = train3_arrival + 20
    total_wait = train4_arrival - train1_arrival
    result = total_wait
    return result

print(solution())