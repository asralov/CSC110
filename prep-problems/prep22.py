def most_common_vehicle(file):
    most_common = open(file, 'r')
    toyota = int(most_common.readline())
    ford = int(most_common.readline())
    chevy = int(most_common.readline())
    if toyota > ford > chevy or toyota > chevy > ford:
        print('Toyota most common')
    if ford > toyota > chevy or ford > chevy > toyota:
        print('Ford most common')
    if chevy > ford > toyota or chevy > toyota > ford:
        print('Chevy most common')
    if toyota == ford or ford == chevy or toyota == chevy:
        print('There\'s a tie!')

