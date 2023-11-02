def solution():
    # Define the average size of a jpeg and the storage capacity of the first iPhone
    jpeg_size = 20 # in kb
    iphone_storage = 16 # in GB, 1 GB = 1000000 kb
    
    # Calculate how many kb can fit in the iPhone's storage
    total_storage = iphone_storage * 1000000
    
    # Calculate how many jpegs can fit in the total storage
    total_jpegs = total_storage / jpeg_size
    
    # Check if 100,000 jpegs can fit in the total storage
    if total_jpegs >= 100000:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())