with open('output.txt', 'w+') as file1:
    in1 = input('Enter text to write to the file: ')
    file1.write(in1)
    print("Data successfully written to output.txt")
    in2 = input('Enter additional text to append: ')
    file1.write("\n"+in2)
    print("Data successfully appended.")
with open('output.txt', 'r') as file2:
        print("Final contents of output.txt :\n", file2.read())
