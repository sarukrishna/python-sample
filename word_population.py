from matplotlib import pyplot


def world_population():
    world_txt = open("world_population.txt", 'r').readlines()
    x_values = []
    y_values = []
    for point in world_txt:
        x_value, y_value = point.split()
        x_values.append(x_value)
        y_values.append(y_value)

    pyplot.plot(x_values, y_values, "o-")
    pyplot.ylabel("values")
    pyplot.xlabel("Time")
    pyplot.title("The time graph")
    pyplot.show()


def women_population():
    data = open("world_population.txt", "r").readlines()
    dates = []
    female_list = []
    male_list = []
    print(data)
    for point in data:
	    date, female, male = point.split(',')
        dates.append(date)
        female_list.append(female)
        male_list.append(male)
		
    pyplot.plot(dates, female_list, "bo-", label="female")
    pyplot.plot(dates, male_list, "mo-", label="male")
    pyplot.show()

women_population()



	
