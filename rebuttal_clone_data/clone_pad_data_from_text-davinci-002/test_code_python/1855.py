def solution():
     percentage_of_citizens_with_pets = 60
     percentage_of_citizens_with_dogs = 50
     percentage_of_citizens_with_cats = 30
     citizens_with_pets = percentage_of_citizens_with_pets / 100
     citizens_with_dogs = percentage_of_citizens_with_dogs / 100
     citizens_with_cats = percentage_of_citizens_with_cats / 100
     total_citizens = citizens_with_pets / (citizens_with_dogs + citizens_with_cats)
     result = total_citizens
     return result

print(solution())