

def sphere(mass:float,radius:float):
    #https://scienceworld.wolfram.com/physics/MomentofInertiaSphere.html
    Ixx = (2/3) * mass * radius**2
    Iyy = (2/3) * mass * radius**2
    Izz = (2/3) * mass * radius**2
    Ixy = 0
    Ixz = 0
    Iyz = 0
    #format
    #<inertia ixx="0.000252666666667" ixy="0" ixz="0" iyy="0.000252666666667" iyz="0" izz="0.0005"/>
    return [Ixx,Ixy,Ixz,Iyy,Iyz,Izz]

def cylinder(mass:float,radius:float,height:float):
    #https://scienceworld.wolfram.com/physics/MomentofInertiaCylinder.html
    Ixx = (1/12) * mass *height**2 + 1/4*  mass *radius**2
    Iyy = (1/12) * mass *height**2 + 1/4*  mass *radius**2
    Izz = (1/2) * mass * radius**2
    Ixy = 0
    Ixz = 0
    Iyz = 0
    return [Ixx,Ixy,Ixz,Iyy,Iyz,Izz]


def box(mass:float,width:float, depth:float,height:float):
    #length x, depth y, height z
    Ixx = (1/12) * mass *(height**2 + depth**2)
    Iyy = (1/12) * mass *(height**2 + width**2)
    Izz = (1/2) * mass *(depth**2 + width**2)
    Ixy = 0
    Ixz = 0
    Iyz = 0
    return [Ixx,Ixy,Ixz,Iyy,Iyz,Izz]


#root Link: link_base has 6 child(ren)
#    child(1):  link_caster_back
#    child(2):  link_base_footprint
#    child(3):  link_caster_front
#<sphere radius=".05"/>
#    child(4):  link_laser_front_scan
#    child(5):  link_left_wheel
#<cylinder radius=".05" length=".05" />
#    child(6):  link_right_wheel

print(("base_link",cylinder(25,.5,.3)))
print(("link_casters",sphere(1,.05)))
print(("link_wheels",cylinder(1,.05,.05)))


