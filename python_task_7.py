try:
    with open("sample.txt","r+") as file1:
        file_data = file1.readlines()
except FileNotFoundError:
    print("Error: The File 'sample.txt' was not found.")
else:
    for i in range(len(file_data)):
        print("Line ", i+1, ":", file_data[i])
finally:
    print()