def solution():
		total_cookies = 120
		adult_share = total_cookies * (1/3)
		cookies_for_kids = total_cookies - adult_share
		cookies_per_kid = cookies_for_kids / 4
		result = cookies_per_kid
		return result

print(solution())