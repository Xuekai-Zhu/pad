def solution():
	total_cookies = 70
	cookies_left = 28
	cookies_gone = total_cookies - cookies_left
	cookies_taken_out = cookies_gone / 7
	cookies_taken_out_4_days = cookies_taken_out * 4
	result = cookies_taken_out_4_days
	return result

print(solution())