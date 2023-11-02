def solution():
    """Harly's animal shelter has 80 dogs. She adopts out 40% of them but then has to take back 5 because of personality conflicts with other dogs in their adopted homes. How many dogs does she have now?"""
    initial_dogs = 80
    adopted_out = initial_dogs * 0.4
    returned = 5
    remaining_dogs = initial_dogs - adopted_out + returned
    result = remaining_dogs
    return result

print(solution())