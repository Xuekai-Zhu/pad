def solution():
    # Calculate the number of cats on the street
    cats = (2/3) * 300  

    # Calculate the number of dogs on the street
    dogs = 300 - cats  

    # Calculate the total number of dog legs on the street
    dog_legs = dogs * 4  

    result = dog_legs
    return result

print(solution())