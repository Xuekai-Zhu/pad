def solution():
    
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