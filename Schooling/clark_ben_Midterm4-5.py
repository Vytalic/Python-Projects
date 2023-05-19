# Ben Clark
# CSCI II 161 L03
# Midterm Exam 4/5

# Empty List for User Input
my_list = []
list_length = 5

ordered = ['first', 'second', 'third', 'fourth', 'fifth']

for names in range(list_length):
    print('Enter the ', ordered[names], ' name.')
    name = input()
    print()
    my_list.append(name)

my_list.sort()
print(my_list)