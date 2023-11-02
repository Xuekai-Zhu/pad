def solution():
    # Calculate the total amount of coffee Jack makes in 24 days
    total_batches = 24 / 2  # Jack makes a batch every 2 days
    total_gallons = total_batches * 1.5  # each batch is 1.5 gallons
    total_ounces = total_gallons * 128  # 1 gallon is 128 ounces
    # Calculate the total time Jack spends making coffee
    total_time = total_batches * 20  # it takes 20 hours to make one batch
    # Calculate the time he spends making coffee in 24 days
    time_in_24_days = total_time / (24 / 2)  # 24/2 = 12 is the number of batches he makes in 24 days
    result = time_in_24_days  # in hours
    return result

print(solution())