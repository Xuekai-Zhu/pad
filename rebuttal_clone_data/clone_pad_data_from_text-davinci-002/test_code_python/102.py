def solution():
     """Ellie has found an old bicycle in a field and thinks it just needs some oil to work well again. She needs 10ml of oil to fix each wheel and will need another 5ml of oil to fix the rest of the bike. How much oil does she need in total to fix the bike?"""
     wheels = 2
     oil_per_wheel = 10
     oil_for_rest_of_bike = 5
     total_oil = wheels * oil_per_wheel + oil_for_rest_of_bike
     result = total_oil
     return result

print(solution())