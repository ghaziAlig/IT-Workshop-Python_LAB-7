file = open("integers.txt","r")
while True:
    line = file.readline()
    try:
        line = int(line)
        if line%2 == 0:
            file1 = open("even.txt", "a")
            file1.write(str(line))
            file1.write("\n")
            file1.close()
        else:
            file2 = open("odd.txt","a")
            file2.write(str(line))
            file2.write("\n")
            file2.close()
        if not line:
            break
    except ValueError:
        break
print(file1.name)
print(file2.name)
file.close()
