def solution():
    """Harly's animal shelter has 80 dogs. She adopts out 40% of them but then has to take back 5 because of personality conflicts with other dogs in their adopted homes. How many dogs does she have now?"""
    initial_dogs = 80
    adopted_dogs = int(initial_dogs * 0.4)
    returned_dogs = 5
    remaining_dogs = initial_dogs - adopted_dogs + returned_dogs
    result = remaining_dogs
    return result

print(solution())