# Ben Clark
# CSCI II 161 L03
# Midterm Exam 3/5

# Clamp Function Definition
def clamp(Uinput):
    if Uinput < 0:
        return 0
    elif Uinput > 255:
        return 255
    else:
        return Uinput

# Program Objective
Uinput = int(input("\nPlease type a number and press 'enter': "))

print('\n', clamp(Uinput), '\n')