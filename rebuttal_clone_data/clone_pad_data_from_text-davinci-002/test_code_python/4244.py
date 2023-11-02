def solution():
     chickens_bought = 10 + 6 - 5
     chickens_taken_by_mary = chickens_bought - 6
     chickens_taken_by_john = chickens_taken_by_mary + 5
     chickens_taken_by_ray = chickens_taken_by_mary - 10
     chickens_more_taken_by_john = chickens_taken_by_john - chickens_taken_by_ray
     result = chickens_more_taken_by_john
     return result

print(solution())