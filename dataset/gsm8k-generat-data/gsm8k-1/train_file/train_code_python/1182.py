def solution():
    """A small zoo houses a variety of 68 wild animals. After they send a gorilla family of six to a different zoo, they adopt a hippopotamus from another zoo. A while later, an animal rescue contacted them, and the zoo took in three endangered rhinos. Then one of their lionesses gave birth to cubs, and they opened a meerkat exhibit with twice as many meerkats as they had gained lion cubs. The zoo then had 90 animals in all. How many lion cubs were born at the zoo?"""
    initial_animals = 68
    gorillas_sent = 6
    hippopotamus_added = 1
    rhinos_added = 3
    meerkats = 2
    lions = 0
    
    # Calculate current number of animals
    current_animals = initial_animals - gorillas_sent + hippopotamus_added + rhinos_added
    
    # Calculate number of lion cubs
    for i in range(1, current_animals+1):
        if (current_animals - i) + i*meerkats == 90:
            lions = i
            break
    
    result = lions
    
    return result

print(solution())