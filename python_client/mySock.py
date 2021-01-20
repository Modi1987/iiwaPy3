# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:21:02 2018
Updated on Mon Oct 21 15:51:03 2019
@author: Mohammad SAFEEA
"""
import socket
import time


class mySock:
    '''demonstration class only
      - coded for clarity, not efficiency
    '''

    def __init__(self, tup,trans=(0,0,0,0,0,0)):
        try:
            LENGTH=len(trans)
        except:
            print('Error: TCP transform shall be a tuple of 6')
            return
        if not(LENGTH==6):
            print('Error: TCP transform shall be a tuple of 6')
            print('Program terminated')
            return
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(tup)
        except:
            print('Error, could not establish a connection to the robot')
        time.sleep(1)
        # self.buff = StringIO.StringIO(2048)  
        # Update the transform of the TCP if one is specified
        flag=False
        for num in trans:
            if not(num==0):
                flag=True
                break
        if flag==False:
            print('No TCP transofrm in Flange Frame is defined,')
            print('The following (default) TCP transform is utilized')
            print(trans)
            return
        else:
            # Rrint info about the current operation
            print('Trying to mount the follwoing TCP transform:')
            stringTuple=('x (mm)','y (mm)','z (mm)','alfa (rad)','beta (rad)','gamma (rad)')
            for i in range(6):
                print(stringTuple[i]+': '+str(trans[i]))
            # Try to mount the TCP
            daMessage='TFtrans'
            for num in trans:
                daMessage=daMessage + '_'
                daMessage=daMessage + str(num)
            daMessage=daMessage + '\n'
            # command=self.buff.getvalue()
            # self.buff.truncate(0)
            #print(command)
            try:
                self.send(command)
                returnAckNack=self.receive()
                #print(returnAckNack)
                if returnAckNack.find('done')==-1:
                    print('Error could not mount the specified Tool')
                else:
                    print('Specified TCP transform mounted successfully')
            except:
                print('Error, (exception) could not mount the specified TCP')
            
    def send(self, msg):
        bytes=msg.encode()
        self.sock.send(bytes)

    def receive(self):
        daBytes=self.sock.recv(1024)
        confirmationMessage=daBytes.decode('utf-8')
        return confirmationMessage;
        

        
    def close(self):
        endCommand='end\n'
        self.send(endCommand)
        time.sleep(1) # sleep for one seconds
        self.sock.close()
