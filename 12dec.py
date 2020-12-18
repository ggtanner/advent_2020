import math

input_file = open("C:\\Users\\Geoff\\Documents\\advent_of_code_2020\\12dec_input.txt","r")

navigations = input_file.readlines()

current_vector = 0

"""# part i
for step in navigations:
    direction = step[0]
    magnitude = int(step[1:])

    if direction == 'F':
        current_x_pos += math.cos(current_vector) * magnitude
        current_y_pos += math.sin(current_vector) * magnitude
    if direction == 'N':
        current_y_pos += magnitude
    if direction == 'S':
        current_y_pos -= magnitude
    if direction == 'E':
        current_x_pos += magnitude
    if direction == 'W':
        current_x_pos -= magnitude
    if direction == 'L':
        current_vector += (magnitude) * (math.pi/180) 
    if direction == 'R':
        current_vector -= (magnitude) * (math.pi/180) 

manhattan_distance = abs(current_x_pos) + abs(current_y_pos)
print("x_distance " + str(current_x_pos))
print("y_distance " + str(current_y_pos))
print("manhattan_distance " + str(manhattan_distance))"""

current_x_pos_ship = 0 # East +, West -
current_y_pos_ship = 0 # North +, South -
relative_x_pos_waypoint = 10
relative_y_pos_waypoint = 1
absolute_x_pos_waypoint = current_x_pos_ship + relative_x_pos_waypoint
absolute_y_pos_waypoint = current_y_pos_ship + relative_y_pos_waypoint

# part 2
for step in navigations:
    direction = step[0]
    magnitude = int(step[1:])

    if direction == 'F':
        current_x_pos_ship += magnitude*relative_x_pos_waypoint
        current_y_pos_ship += magnitude*relative_y_pos_waypoint
    if direction == 'N':
        relative_y_pos_waypoint += magnitude
    if direction == 'S':
        relative_y_pos_waypoint -= magnitude
    if direction == 'E':
        relative_x_pos_waypoint += magnitude
    if direction == 'W':
        relative_x_pos_waypoint -= magnitude
    if direction == 'L':
        current_angle = math.atan2(relative_y_pos_waypoint,relative_x_pos_waypoint)
        relative_magnitude = math.sqrt((relative_x_pos_waypoint**2) + (relative_y_pos_waypoint**2))
        rot_angle = magnitude * (math.pi/180)
        new_angle = current_angle + rot_angle
        relative_x_pos_waypoint = relative_magnitude * math.cos(new_angle)
        relative_y_pos_waypoint = relative_magnitude * math.sin(new_angle)
    if direction == 'R':
        current_angle = math.atan2(relative_y_pos_waypoint,relative_x_pos_waypoint)
        relative_magnitude = math.sqrt((relative_x_pos_waypoint**2) + (relative_y_pos_waypoint**2))
        rot_angle = magnitude * (math.pi/180)
        new_angle = current_angle - rot_angle
        relative_x_pos_waypoint = relative_magnitude * math.cos(new_angle)
        relative_y_pos_waypoint = relative_magnitude * math.sin(new_angle)
        
    absolute_x_pos_waypoint = current_x_pos_ship + relative_x_pos_waypoint
    absolute_y_pos_waypoint = current_y_pos_ship + relative_y_pos_waypoint

manhattan_distance = abs(current_x_pos_ship) + abs(current_y_pos_ship)
print("x_distance " + str(current_x_pos_ship))
print("y_distance " + str(current_y_pos_ship))
print("manhattan_distance " + str(manhattan_distance))