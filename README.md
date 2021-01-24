

# iiwaPy3

Python3 librarry used to control KUKA iiwa robots, the 7R800 and the 14R820, from an external computer.

Using the iiwaPy3 the utilizer can control the iiwa robot from his/her computer without a need for programming  the industerial manipulator.

A basic knowledge of using python is required.


--------------------------------------

# Required packages

The iiwaPy3 is a Python3 wrapper for the KUKA sunrise toolbox, [found in here](https://github.com/Modi1987/KST-Kuka-Sunrise-Toolbox).
To utilize the iiwaPy3, you have to install the [KST Server (Java Application)](https://github.com/Modi1987/KST-Kuka-Sunrise-Toolbox/tree/master/KUKA_Sunrise_server_source_code) into the Kuka iiwa controller using the Sunrise.Workbench.


--------------------------------------

# Video tutorials

Video tutorials on controlling IIWA from python [are available in here](https://www.youtube.com/watch?v=QkUe8JIs63A&list=PLz558OYgHuZdRoxkqQ-M9LOdksZnEWbKq&index=2&t=0s).


--------------------------------------

# To test the iiwaPy3

To test the iiwaPy3 follow the steps:

## On PC side:
1- Establish a peer to peer connection between the PC and the robot, [described in videos 1 and 2 of the play list](https://www.youtube.com/playlist?list=PLz558OYgHuZd-Gc2-OryITKEXefAmrvae);

2- Synchronise the [KST Server (Java Application)](https://github.com/Modi1987/KST-Kuka-Sunrise-Toolbox/tree/master/KUKA_Sunrise_server_source_code) into the robot controller using the Sunrise.Workbench;

## On the robot side:
1- Run the application "MatlabToolboxServer" from the smartPad of the robot.

2- Note that you have 60 seconds to connect from Python3 before the server is shutdown automatically. In case you did not establish a connection within the 60 seconds, you have to start again the "MatlabToolboxServer" application from the smartPad of the robot .

## From Python on your PC
From inside python IDE run the tutorial script [Tutorial_getters, available here](https://github.com/Modi1987/iiwaPy/blob/master/python_client/Tutorial_getters.py), you shall see data acquired from the robot controller printed inside python console.

(All python files starting with "Tutorial" are tutorial scripts written around iiwaPy3 class to control the robot)


--------------------------------------

Copyright: Mohammad Safeea, first commit 20th-Jan-2021

