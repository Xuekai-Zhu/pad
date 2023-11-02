def solution():
     total_dolphins = 20
     dolphins_trained = total_dolphins / 4
     dolphins_in_training = (total_dolphins - dolphins_trained) * (2/3)
     dolphins_to_be_trained = total_dolphins - dolphins_trained - dolphins_in_training
     result = dolphins_to_be_trained
     return result

print(solution())