import urllib2
import re

url_adres = "http://www.python-challenges.com/ftwp/SEYMELTJ/amaze/maze"
open_url = urllib2.urlopen(url_adres)
html_tree = open_url.read()
maze_elements = re.findall('<rect fill="[a-z]*" height="[0-9]*" width="[0-9]*" x="[0-9]*" y="[0-9]*" \57>', html_tree)
split_maze_elements = []
dane = {}
maze_data = {}
for tooling in maze_elements:
    split_maze_elements.append(tooling.split(","))
start = 0
loop = 0
for tooling in split_maze_elements:

    element = tooling[0].split('<rect fill=')
    element = "".join(element)
    element = element.split('height=')
    element = "".join(element)
    element = element.split('width=')
    element = "".join(element)
    element = element.split('x=')
    element = "".join(element)
    element = element.split('y=')
    element = "".join(element)
    element = element.split(' />')
    element = "".join(element)
    element = element.split(' ')

    maze_data[loop] = {"fill": element[0],
                       "height": element[1],
                       "width": element[2],
                       "x": element[3],
                       "y": element[4]}
    if element[1] == element[3] and element[2] == element[4]:
        start = loop
    loop = loop+1

jump = 0

while True:
    if int(maze_data[jump]["y"][1:-1]) > 0:
        break
    jump = jump+1


def finding_way(obejct):
    obejct.chechikng()
    while maze_data[obejct.position]["fill"] != '"red"':
        while obejct.crosses[obejct.crosses_number]["left"] == True:
            if obejct.x_side-obejct.size > 0 and maze_data[obejct.position-1]["fill"] != '"black"':
                if maze_data[obejct.position-1]["fill"] == '"red"':
                    obejct.left()
                    object.crosses[object.crosses_number]["last"] = "left"
                    return
                if obejct.crosses[obejct.crosses_number]["last"] != "right":
                    obejct.left()
                    obejct.chechikng()
                    obejct.crosses[obejct.crosses_number]["right"] = False
        while obejct.crosses[obejct.crosses_number]["down"] == True:
            if obejct.y_side + obejct.size > 0 and maze_data[obejct.position + obejct.jump]["fill"] != '"black"':
                if maze_data[obejct.position + obejct.jump]["fill"] == '"red"':
                    obejct.down()
                    object.crosses[object.crosses_number]["last"] = "down"
                    return
                if obejct.crosses[obejct.crosses_number]["last"] != "up":
                    obejct.down()
                    obejct.chechikng()
                    obejct.crosses[obejct.crosses_number]["up"] = False
        while obejct.crosses[obejct.crosses_number]["right"] == True:
            if maze_data[obejct.position+1]["fill"] != '"black"':
                if maze_data[obejct.position+1]["fill"] == '"red"':
                    obejct.right()
                    object.crosses[object.crosses_number]["last"] = "right"
                    return
                if obejct.crosses[obejct.crosses_number]["last"] != "left":
                    obejct.right()
                    obejct.chechikng()
                    obejct.crosses[obejct.crosses_number]["left"] = False
        while obejct.crosses[obejct.crosses_number]["up"] == True:
            if obejct.y_side - obejct.size > 0 and maze_data[obejct.position - obejct.jump]["fill"] != '"black"':
                if maze_data[obejct.position - obejct.jump]["fill"] == '"red"':
                    obejct.up()
                    object.crosses[object.crosses_number]["last"] = "up"
                    return
                if obejct.crosses[obejct.crosses_number]["last"] != "down":
                    obejct.up()
                    obejct.chechikng()
                    obejct.crosses[obejct.crosses_number]["down"] = False

        if obejct.crosses[obejct.crosses_number]["right"] == False and obejct.crosses[obejct.crosses_number]["left"] == False:
            if obejct.crosses[obejct.crosses_number]["up"] == False and obejct.crosses[obejct.crosses_number]["down"] == False:
                del obejct.crosses[obejct.crosses_number]
                obejct.crosses_number = obejct.crosses_number - 1
                obejct.x_side = int(maze_data[obejct.crosses[obejct.crosses_number]["position"]]["x"][1:-1])
                obejct.y_side = int(maze_data[obejct.crosses[obejct.crosses_number]["position"]]["y"][1:-1])
                obejct.position = obejct.crosses[obejct.crosses_number]["position"]
                obejct.crosses[obejct.crosses_number]["last"] = ""


class Me():
    def __init__(self):
        self.x_side = int(maze_data[start]["x"][1:-1])
        self.y_side = int(maze_data[start]["y"][1:-1])
        self.fill = "green"
        self.position = start
        self.size = self.x_side
        self.jump = jump
        self.crosses_number = 0
        self.crosses = {}

    def __getitem__(self, item):
        return(self.crosses)[item]

    def right(self):
        if (self.x_side+self.size)%self.size == 0 and maze_data[self.position+1]["fill"] == '"white"':
            self.x_side = self.x_side+self.size
            self.crosses[self.crosses_number]['position'] = self.position
            self.position = self.position+1
            self.crosses[self.crosses_number]['right'] = False
            self.crosses[self.crosses_number]["last"] = "right"

    def left(self):
        if self.x_side-self.size > 0 and maze_data[self.position-1]["fill"] == '"white"':
            self.x_side = self.x_side-self.size
            self.crosses[self.crosses_number]['position'] = self.position
            self.position = self.position - 1
            self.crosses[self.crosses_number]['left'] = False
            self.crosses[self.crosses_number]["last"] = "left"

    def up(self):
        if self.y_side-self.size > 0 and maze_data[self.position-self.jump]["fill"] == '"white"':
            self.y_side = self.y_side-self.size
            self.crosses[self.crosses_number]['position'] = self.position
            self.position = self.position-self.jump
            self.crosses[self.crosses_number]['up'] = False
            self.crosses[self.crosses_number]["last"] = "up"

    def down(self):
        if self.y_side+self.size > 0 and maze_data[self.position+self.jump]["fill"] == '"white"':
            self.y_side = self.y_side+self.size
            self.crosses[self.crosses_number]['position'] = self.position
            self.position = self.position+self.jump
            self.crosses[self.crosses_number]['down'] = False
            self.crosses[self.crosses_number]["last"] = "down"

    def chechikng(self):
        if self.crosses_number in self.crosses.keys():
            self.crosses_number = self.crosses_number + 1
        if not self.crosses_number in self.crosses.keys():
            self.crosses[self.crosses_number] = {"up": False,
                                                 "down": False,
                                                 "left": False,
                                                 "right": False,
                                                 "position": 0,
                                                 "last": ""}

        if maze_data[self.position-self.jump]['fill'] != '"black"':
            self.crosses[self.crosses_number]["up"] = True
        if maze_data[self.position+self.jump]['fill'] != '"black"':
            self.crosses[self.crosses_number]["down"] = True
        if maze_data[self.position-1]["fill"] != '"black"':
            self.crosses[self.crosses_number]["left"] = True
        if maze_data[self.position+1]["fill"] != '"black"':
            self.crosses[self.crosses_number]["right"] = True


object = Me()
finding_way(object)
answer = ""
for i in object.crosses:
    if object[i]["last"] == "right":
        answer = answer+"R"
    elif object[i]["last"] == "left":
        answer = answer + "L"
    elif object[i]["last"] == "up":
        answer = answer + "T"
    elif object[i]["last"] == "down":
        answer = answer + "B"
print(answer)
print(object.crosses_number)
print(len(answer))
