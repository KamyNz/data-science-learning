import research


# define main method
def main():
	print("Weather research for Seattle, 2014-2015")
	print()

	# TODO: Initialize the data
	research.init()
	#print(research.data)
	
	print("The hottest 5 days:")
	days = research.hot_days()
	#TODO: Show the days, creating a function that gives the hottest 5 days
	for idx,d in enumerate(days[:5]):
		print("{}. {} F on {}".format(idx+1,d.actual_max_temp, d.date))

	print()
	print("The coldest 5 days:")
	days = research.cold_days()
	#TODO: Show the days
	for idx,d in enumerate(days[:5]):
		print("{}. {} F on {}".format(idx+1,d.actual_min_temp, d.date))

	print()

	print("The wettest 5 days:")
	#TODO: Show the days
	days = research.wet_days()
	# TODO: Show the days
	for idx, d in enumerate(days[:5]):
		print("{}. {} F on {}".format(idx + 1, d.actual_precipitation, d.date))


if __name__ == '__main__':
	main()

