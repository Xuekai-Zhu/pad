def solution():
     initial_amount = 4000
     first_client = initial_amount / 2
     second_client = initial_amount * 2 / 5
     third_client = initial_amount + (first_client + second_client)
     total_amount = first_client + second_client + third_client
     result = total_amount
     
     return result

print(solution())