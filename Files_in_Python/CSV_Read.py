file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    persona_data = line.split(',')
    name = persona_data[0]
    age = persona_data[1]
    university = persona_data[2]
    degree = persona_data[3]
    print (f' {name.title()},is at age {age}, Now studying in {university.title()} on {degree.title()}')
