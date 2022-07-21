# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     # needs to close the file to free up the resources of the computer

with open("new_file.txt", mode="w") as file:
    file.write("The new file")

with open("../../my_file.txt") as file:
    contents = file.read()
    print(contents)
