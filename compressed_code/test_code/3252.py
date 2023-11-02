def solution():
    
    cantaloupe_start = 30
    honeydew_start = 27
    cantaloupe_dropped = 2
    honeydew_rotten = 3
    cantaloupe_left = 8
    honeydew_left = 9
    cantaloupe_sold = cantaloupe_start - cantaloupe_dropped - cantaloupe_left
    honeydew_sold = honeydew_start - honeydew_rotten - honeydew_left
    cantaloupe_money = cantaloupe_sold * 2
    honeydew_money = honeydew_sold * 3
    total_money = cantaloupe_money + honeydew_money
    result = total_money
    return result

print(solution())