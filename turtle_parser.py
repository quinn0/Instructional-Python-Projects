temp = "Banner"
replaced = temp.replace("n", "l")
print(temp)
print(replaced)
from turtle import * #Turtle library
dim = 200
setworldcoordinates(-1*dim, -1*dim, dim, dim)
shape("turtle")
test = "F50L60F40R20F60B90R30F80R90F80B50L80F80"

ps = [] #list of positions as tuples
test_ps = [(50.00,0.00), (50.00,0.00), (50.00,0.00), (50.00,0.00), (50.00,0.00), (50.00,0.00), (50.00,0.00), (50.00,0.00), (70.00,34.64), (70.00,34.64), (70.00,34.64), (70.00,34.64), (70.00,34.64), (70.00,34.64), (70.00,34.64), (70.00,34.64), (115.96,73.21), (115.96,73.21), (115.96,73.21), (115.96,73.21), (47.02,15.36), (47.02,15.36), (47.02,15.36), (47.02,15.36), (47.02,15.36), (47.02,15.36), (47.02,15.36), (47.02,15.36), (-31.77,1.47), (-31.77,1.47), (-31.77,1.47), (-31.77,1.47), (-31.77,1.47), (-31.77,1.47), (-31.77,1.47), (-31.77,1.47), (-45.66,80.25), (-45.66,80.25), (-45.66,80.25), (-45.66,80.25), (-36.98,31.01), (-36.98,31.01), (-36.98,31.01), (-36.98,31.01), (-36.98,31.01), (-36.98,31.01), (-36.98,31.01), (-36.98,31.01), (43.02,31.01), (43.02,31.01)]
def turtle_parserTeacher(dir_str):
    penup()
    color("red")
    speed(0)
    for i in range(len(dir_str) - 2):
        if dir_str[i] == "R": #turn right
            #note: if we generalize beyond 2 digits
            #they could use a while loop inside
            #but significantly harder (I think)
            angle = int(dir_str[i+1:i+3])
            right(angle)
            ps.append(pos())
        if dir_str[i] == "L": #turn left
            angle = int(dir_str[i+1:i+3]) 
            ps.append(pos())
            left(angle)

        if dir_str[i] == "F": #fowards 
            dist = int(dir_str[i+1:i+3])
            fd(dist)
            ps.append(pos()) 


        if dir_str[i] == "B": #backwards 
            dist = int(dir_str[i+1:i+3]) 
            left(180)
            fd(dist)
            ps.append(pos())

        ps.append(pos())
            
    # done()
# turtle_parserTeacher(test)            

#Place stamps at each turning point
#to check for correct path
def goal_marker(turn_pt): 
    penup()
    goto((0,0))
    speed(0)
    for coord in turn_pt:
        goto(coord)
        stamp()
    # done()

###Student solution
def turtle_parser(dir_str):
    goal_marker(test_ps)
    speed(3)
    goto((0,0))
    pendown()
    color("black")
    for i in range(len(dir_str) - 2):
        if dir_str[i] == "R": #turn right
            angle = int(dir_str[i+1:i+3])
            right(angle)
        if dir_str[i] == "L": #turn left
            angle = int(dir_str[i+1:i+3]) 
            left(angle)
        if dir_str[i] == "F": #fowards 
            dist = int(dir_str[i+1:i+3]) 
            fd(dist)
        if dir_str[i] == "B": #backwards 
            dist = int(dir_str[i+1:i+3]) 
            left(180)
            fd(dist)
    done()

turtle_parser(test) 
# print(ps)

#### With Color###
colormode(255)

def col_parse(col_str):
    col_clean = col_str.replace( "(","").replace(")", "")
    col_list = col_clean.split(",")
    color(int(col_list[0]), int(col_list[1]), int(col_list[2]))

test = "C(255,0,102)F50L60C(102,0,102)F40R20C(255,51,255)F60C(0,51,153)B90R30C(255,51,0)F80R90C(30,30,30)F80C(0,153,51)B50L80C(10,40,90)F80"

def turtle_parser_col(dir_str):
    width(10)
    for i in range(len(dir_str)-2):
        if dir_str[i] == "C": #must .index() with slice to pass to col_parse
            start = dir_str[i:].index("(")
            end =  dir_str[i:].index(")")
            col_parse(dir_str[i+start:i+end+1])
        else:
            if dir_str[i] == "R": #turn right
                angle = int(dir_str[i+1:i+3])
                right(angle)
            if dir_str[i] == "L": #turn left
                angle = int(dir_str[i+1:i+3]) 
                left(angle)
            if dir_str[i] == "F": #fowards 
                dist = int(dir_str[i+1:i+3]) 
                fd(dist)
            if dir_str[i] == "B": #backwards 
                dist = int(dir_str[i+1:i+3]) 
                left(180)
                fd(dist)
    done()


speed(1)
# turtle_parser_col(test)