def solution():
    credit_card_statement = 500
    couch_cost = 750
    table_cost = 100
    lamp_cost = 50
    total_cost = couch_cost + table_cost + lamp_cost
    amount_still_owed = total_cost - credit_card_statement
    result = amount_still_owed
    return result

print(solution())