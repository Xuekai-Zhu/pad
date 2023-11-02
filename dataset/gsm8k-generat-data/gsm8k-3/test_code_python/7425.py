def solution():
    """Lars owns a bakeshop. She can bake 10 loaves of bread within an hour and 30 baguettes every 2 hours. If she bakes 6 hours a day, how many breads does she makes?"""
    # Calculate the number of loaves of bread Lars can bake in 6 hours
    bread_hours = 6
    bread_hours_per_batch = 1
    breads_per_batch = 10
    num_bread_batches = bread_hours // bread_hours_per_batch
    breads_per_hour = breads_per_batch * num_bread_batches
    total_breads = breads_per_hour * bread_hours

    # Calculate the number of baguettes Lars can bake in 6 hours
    baguette_hours = 6
    baguette_hours_per_batch = 2
    baguettes_per_batch = 30
    num_baguette_batches = baguette_hours // baguette_hours_per_batch
    baguettes_per_hour = baguettes_per_batch * num_baguette_batches
    total_baguettes = baguettes_per_hour * baguette_hours

    # Calculate the total number of breads Lars makes
    total_breads_made = total_breads + (total_baguettes / 3)

    # Display the total number of breads
    result = total_breads_made
    return result

print(solution())