def solution():
     bottles_of_milk = 35
     bottles_purchased_by_jason = 5
     bottles_purchased_by_harry = 6
     bottles_left = bottles_of_milk - (bottles_purchased_by_jason + bottles_purchased_by_harry)
     result = bottles_left
     return result

print(solution())