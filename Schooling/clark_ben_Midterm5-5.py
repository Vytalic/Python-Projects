# Ben Clark
# CSCI II 161 L03
# Midterm Exam 5/5

# Global variables
tail_number = 0
latitude = 0
longitude = 0
altitude = 0
heading = 0
speed = 0
iterator = 0

aircraftDictionary = {
        'tail_number': tail_number,
        'latitude': latitude,
        'longitude': longitude,
        'altitude': altitude,
        'heading': heading,
        'speed': speed
    }

plane1dict = {}
plane2dict = {}
plane3dict = {}

# Begin Aircraft Class Definition
class Aircraft:

    def __init__(self, tail_number, latitude, longitude, altitude, heading, speed):
        self.tail_number = tail_number
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.heading = heading
        self.speed = speed
        
    def print_plane(self):
        
        print('\n\n-------------Plane 1 -------------')
        print(plane1dict)
        
        print('\n\n-------------Plane 2 -------------')
        print(plane2dict)
        
        print('\n\n-------------Plane 3 -------------')
        print(plane3dict)


# End Aircraft Class Defintion    

# Begin function definition
def tedious(x):
    if x == 1:           
        plane1dict['tail_number'] = input('\nWhat is the tail number? ==> ')
        plane1dict['latitude'] = input('\nWhat is the latitude?    ==> ')
        plane1dict['longitude'] = input('\nWhat is the longitude?   ==> ')
        plane1dict['altitude'] = input('\nWhat is the altitude?    ==> ')
        plane1dict['heading'] = input('\nWhat is the heading?     ==> ')
        plane1dict['speed'] = input('\nWhat is the speed?       ==> ')
    elif x ==2:
        plane2dict['tail_number'] = input('\nWhat is the tail number? ==> ')
        plane2dict['latitude'] = input('\nWhat is the latitude?    ==> ')
        plane2dict['longitude'] = input('\nWhat is the longitude?   ==> ')
        plane2dict['altitude'] = input('\nWhat is the altitude?    ==> ')
        plane2dict['heading'] = input('\nWhat is the heading?     ==> ')
        plane2dict['speed'] = input('\nWhat is the speed?       ==> ')
    elif x ==3:
        plane3dict['tail_number'] = input('\nWhat is the tail number? ==> ')
        plane3dict['latitude'] = input('\nWhat is the latitude?    ==> ')
        plane3dict['longitude'] = input('\nWhat is the longitude?   ==> ')
        plane3dict['altitude'] = input('\nWhat is the altitude?    ==> ')
        plane3dict['heading'] = input('\nWhat is the heading?     ==> ')
        plane3dict['speed'] = input('\nWhat is the speed?       ==> ')
# End function defintion

# Main program objective
for three in '333':
    if iterator == 0:
        iterator += 1
        plane1 = Aircraft(tail_number, latitude, longitude, altitude, heading, speed)
        print('\n---------------------------')
        print('Describe the first plane...')
        print('---------------------------')
        tedious(iterator)
        
    elif iterator == 1:
        iterator += 1
        plane2 = Aircraft(tail_number, latitude, longitude, altitude, heading, speed)
        print('\n----------------------------')
        print('Describe the second plane...')
        print('----------------------------')
        tedious(iterator)
       
    elif iterator == 2:
        iterator += 1
        plane3 = Aircraft(tail_number, latitude, longitude, altitude, heading, speed)
        print('\n---------------------------')
        print('Describe the third plane...')
        print('---------------------------')
        tedious(iterator)
        
plane1.print_plane()
print('\n')
input("Program 5/5 is finished. Press 'enter' to exit...")
