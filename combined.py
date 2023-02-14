num = open("number1.txt","r+")           # open the text files
num1 = open("number2.txt","r+")
num2 = open("all_numbers.txt","w")

read_num = num.read()                    # read the content int the text file
print(read_num)                          # print it out
read_num1 = num1.read()
print(read_num1)
join_list = (f"{read_num} {read_num1}")    # join the content on both text files
list = join_list.split()
list.sort()                                 # set the joined content in asending order
print(list)                      
write_num = num2.write(f"{list}")           # write the content of both files into the next text file


num.close()                                  # close all the text files
num1.close()
num2.close()




