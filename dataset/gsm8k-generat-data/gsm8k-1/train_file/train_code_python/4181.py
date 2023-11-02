def solution():
    """Darryl sells melons on the side of the road. He sells cantaloupes for $2 each and honeydews for $3. He started the day with 30 cantaloupes and 27 honeydews. He accidentally dropped a couple of cantaloupes and three of the honeydews turned out to be rotten. At the end of the day he had 8 cantaloupes and 9 honeydews left. How much money did he make?"""
    cantaloupes_start = 30
    honeydews_start = 27
    cantaloupes_dropped = 2
    honeydews_bad = 3
    cantaloupes_left = 8
    honeydews_left = 9
    cantaloupes_sold = cantaloupes_start - cantaloupes_dropped - cantaloupes_left
    honeydews_sold = honeydews_start - honeydews_bad - honeydews_left
    cantaloupe_money = cantaloupes_sold * 2
    honeydew_money = honeydews_sold * 3
    total_money = cantaloupe_money + honeydew_money
    result = total_money
    
    return result

print(solution())