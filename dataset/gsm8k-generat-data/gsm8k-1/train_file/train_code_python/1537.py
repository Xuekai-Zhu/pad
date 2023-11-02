def solution():
    """Marcus has received a commission for as many paintings as possible. Marcus plans out his drawings so that his client can receive some of the paintings as soon as possible but it is still going to take a long time. On the first day, he paints 2 paintings. He then paints every day and each day, he paints twice as many paintings as he painted the day before. If he paints for 5 days, how many paintings will he have painted in total?"""
    paintings_per_day = [2]
    for i in range(1, 5):
        paintings = paintings_per_day[i-1]*2
        paintings_per_day.append(paintings)
    total_paintings = sum(paintings_per_day)
    result = total_paintings
    return result

print(solution())