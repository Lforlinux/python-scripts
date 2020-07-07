
new_name = input('Enter you name')

my_file = open('data.txt', 'r')
file_content = my_file.read()
my_file.close()
print(file_content)

my_file_writing = open('data.txt', 'w')
print (f" {new_name} has been over written")
my_file_writing.write(new_name)

