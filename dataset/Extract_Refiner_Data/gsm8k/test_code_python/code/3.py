def solution():
    
    # Define the size of the file in GB
    FILE_SIZE = 200

    # Calculate the time it takes to download the file in minutes
    download_time = FILE_SIZE / 2

    # Calculate the time it takes to download the file with the install updates
    install_time = download_time * 0.4

    # Calculate the total time it takes to download the file
    total_download_time = download_time + install_time

    # Display the total download time
    result = total_download_time
    return result

print(solution())