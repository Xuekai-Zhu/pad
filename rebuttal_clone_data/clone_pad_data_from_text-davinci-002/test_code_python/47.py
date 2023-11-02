def solution():
     """The file, 90 megabytes in size, downloads at the rate of 5 megabytes per second for its first 60 megabytes, and then 10 megabytes per second thereafter. How long, in seconds, does it take to download entirely?"""
     size_of_file = 90
     initial_rate = 5
     second_rate = 10
     time_to_download = (size_of_file - initial_rate) / second_rate
     result = time_to_download
     return result

print(solution())