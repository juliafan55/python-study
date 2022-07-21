# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()

#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     # reader method creates an object that can be iterated through
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# sum_temps = 0
# for temp in temp_list:
#     sum_temps += temp
#     avg_temp = sum_temps / len(temp_list)
# print(round(avg_temp))

# get data in the columns
# print(data["temp"].mean())
# print(data["temp"].max())


# get data in rows
# print(data[data.day == "Monday"])
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# c_temp = monday.temp
# f_temp = (c_temp * 1.8) + 32
# print(f_temp)

# create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


squirrel_data = pandas.read_csv("squirrel_data.csv")

fur_color = squirrel_data["Primary Fur Color"]
# grey_fur = 0
# cin_fur = 0
# black_fur = 0
count = fur_color.value_counts()
# print(count)
# count.to_csv("squirrel_fur_color.csv")

data = pandas.read_csv("squirrel_data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("fur_color.csv")
