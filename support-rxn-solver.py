# Hi! This is my first person civil code project, so I'm a little excited about this one.
# Code will solve for support reactions for structurally determinate beams
# through equilibrium equations.

# Assumptions: downwards, to the left, and clockwise are considered negative.

# Note: only works with point laods, point moments, and uniformly distrubuted loads. I am not 
# motivated enough right now to do anythingly else besides uniformly distrubuted loads.

# determine type of loading point load, uniformly distributed load, moment
# NEED TO COME BACK AND FIX DISTRIBUTED LOADING
def load_type():
    point_loads_x = []
    point_loads_y = []
    mom_loads = []
    dist_loads = []

    more_loads = True
    while more_loads:
        # check point loads in x direction
        check_point_load_x = input('Does your beam have a point load in the x-direction? Type \'yes\' or \'no\': ')
        if check_point_load_x == 'yes':
            point_load_mag_x = int(input('Input the magnitude of the point load: '))
            point_loads_x.append(point_load_mag_x)
        elif check_point_load_x == 'no':
            pass
        else:
            return('Invalid value. Try again.')

        # check point loads in y direction
        check_point_load_y = input('Does your beam have a point load in the y-direction? Type \'yes\' or \'no\': ')
        if check_point_load_y == 'yes':
            point_load_mag_y = int(input('Input the magnitude of the point load: '))
            point_load_dist_y = int(input('Input the distance of the point load from the support: '))
            point_loads_y.append((point_load_mag_y, point_load_dist_y))
        elif check_point_load_y == 'no':
            pass
        else:
            return('Invalid value. Try again.')

        # check distributed_load = input('Does your beam have a uniformly distributed load? Type \'yes\' or \'no\': ')

        # check moments
        check_moment = input('Does your beam have a moment? Type \'yes\' or \'no\': ')
        if check_moment == 'yes':
            moment_mag = int(input('Input the magnitude of the moment: '))
            mom_loads.append(moment_mag)
        elif check_moment == 'no':
            pass
        else:
            return('Invalid value. Try again.')
        is_there_more = input('Are there more loads? Type \'yes\' or \'no\': ')
        if is_there_more == 'yes':
            more_loads = True
        elif is_there_more == 'no':
            more_loads = False
        else:
            return('Invalid value. Try again.')
    return point_loads_x, point_loads_y, mom_loads, dist_loads

def cantilever_calc(len):
    point_x_data, point_y_data, moment_data, distributed_data = load_type()
    
    # solve for reaction in x direction
    f_x = 0
    for load in point_x_data:
        f_x += load
    r_x = f_x * (-1)

    # solve for reaction in y direction
    f_y = 0
    for load in point_y_data:
        f_y += load[0]
    r_y = f_y * (-1)

    # solve for moment at support
    total_mom = 0
    for load in point_y_data:
        total_mom += load[0] * load[1]
    for mom in moment_data:
        total_mom += mom
    m_r = total_mom * (-1)
    return(r_x,r_y,m_r)

def main():
    # determine length of beam and type of support
    length = int(input('Please enter the length of the beam: '))
    support = 'neither'
    while support != 'cantilever' or support != 'simply supported':
        support = input('Please enter support type. Type \'cantilever\' or \'simply supported\': ')
        if support == 'cantilever':
            print(cantilever_calc(length))
            break
        # elif support == 'simply supported':
        #     simply_supported_calc(length)
        #     break
        else:
            print('Please enter one of the above options. Try again.')
main()