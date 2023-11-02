def solution():
    """A pack of dogs found a pile of bones in the dumpster behind the butcher shop. One by one, the dogs crawled into the dumpster, grabbed a mouthful of bones, and ran off with their newfound treasure. In all, there were 5 dogs. The first dog carried off 3 bones. The second dog carried off 1 less bone than the first dog. The third dog carried off twice as many as the second dog. The fourth dog carried off one bone, and the fifth dog carried off twice the number of bones as the fourth dog carried, leaving no remaining bones in the dumpster. How many bones were in the original pile of bones?"""
    # Define the number of bones carried by each dog
    dog1_bones = 3
    dog2_bones = dog1_bones - 1
    dog3_bones = dog2_bones * 2
    dog4_bones = 1
    dog5_bones = dog4_bones * 2

    # Calculate the total number of bones
    total_bones = dog1_bones + dog2_bones + dog3_bones + dog4_bones + dog5_bones

    # Return the result
    result = total_bones
    return result

print(solution())