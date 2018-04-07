import matplotlib
matplotlib.use('TKAgg') # MacOS mandatory
matplotlib.rcParams['toolbar'] = 'None' # disable figure toolbar
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import irsdk

ir = irsdk.IRSDK()

global brake
global throttle
global clutch

brake = 0
throttle = 0
clutch = 0

def refresh(i):
    global brake

    # Remove first element
    brake_data_list.pop(0)
    clutch_data_list.pop(0)
    throttle_data_list.pop(0)
	
    if ir.startup():
        brake = (ir['Brake'] * 100)
        throttle = (ir['Throttle'] * 100)
        clutch = (100 - (ir['Clutch'] * 100))	
	
    brake_data_list.append(brake)
    clutch_data_list.append(clutch)
    throttle_data_list.append(throttle)
	
    # clear current asix
    ax.clear()

    # set axes title
    #ax.set_title('iRacing Gear History')

    # set x axes label to null
    ax.set_xticklabels([])

    # set y axes
    ax.set_ylim(-1, 110)
    #ax.set_yticklabels([])
    #ax.set_ylabel('YY')

    # Load data
    
    ax.plot(clutch_data_list, 'blue')
    ax.plot(throttle_data_list, 'green')
    ax.plot(brake_data_list, 'red')
    
    # Set background colour
    ax.set_facecolor('black')
    #ax.set_alpha(0.2)
	
    
    # Set background transparency
    #ax.patch.set_alpha(0.5)

# inital data
brake_data_list = [0] * 100
clutch_data_list = [0] * 100
throttle_data_list = [0] * 100

# create figure with size and axes.
fig, ax = plt.subplots(figsize=(20, 1.3125))

# set window title
fig.canvas.set_window_title('iRacing Pedals')

# start a animation on figure refresh every 200ms
ani = animation.FuncAnimation(fig, refresh, interval = 60)
plt.show()
