def solution():
    """Mrs. Rylan has bought 20 packets of tomato seeds and 80 packets of celery seeds to plant. If a packet of tomato seeds costs $40 and a packet of celery seeds costs $30, how much money did she use to buy the seeds?"""
    tomato_packets = 20
    celery_packets = 80
    tomato_cost = 40
    celery_cost = 30
    total_tomato_cost = tomato_packets * tomato_cost
    total_celery_cost = celery_packets * celery_cost
    total_cost = total_tomato_cost + total_celery_cost
    result = total_cost
    return result

print(solution())