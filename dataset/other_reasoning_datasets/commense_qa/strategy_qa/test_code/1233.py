def solution():
    jackfruit_weight = "22-55 lbs"
    has_spikes = True
    if jackfruit_weight < "10 lbs" or not has_spikes:
        result = "yes"
    else:
        result = "no"
    return result

Note: The solution above is not encouraging throwing jackfruit at anyone's head, it simply states that it would not be safe due to the weight and spikes covering the fruit.

print(solution())