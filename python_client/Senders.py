# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:36:18 2018
Modified 3rd-Jan-2021

@author: Mohammad SAFEEA
"""

import math
from GeneralPurpose import getDoubleFromString 

class Senders:
    
    def __init__(self,mysoc):
        self.mysoc=mysoc

    def send(self,data):
        data=data+'\n'
        self.mysoc.send(data)
        message=self.mysoc.receive()
        return message
    
    # EEF command
    def sendEEfPosition(self,x):
        if(len(x)!=6):
            print('Error in sender function [sendEEfPositions]')
            print('EEF position shall be an array of 6 elements')
            return
        num=10000
        buff = 'DcSeCarW_'
        counter=0
        while counter<6:
            if counter<3:
                buff = buff + str(math.ceil(x[counter]*num)/num)
            else:
                buff = buff + str(x[counter])
            buff = buff + '_'            
            counter=counter+1
        buff = buff + '\n'
        self.send(buff)

    def sendEEfPositions(self,x):
        if(len(x)!=6):
            print('Error in sender function [sendEEfPositions]')
            print('EEF position shall be an array of 6 elements')
            return
        num=10000
        buff = 'cArtixanPosition_'
        counter=0
        while counter<6:
            if counter<3:
                buff = buff + str(math.ceil(x[counter]*num)/num)
            else:
                buff = buff + str(x[counter])
            buff = buff + '_'            
            counter=counter+1
        buff = buff + '\n'
        self.send(buff)
        
    # EEF command with feedback
    def sendEEfPositionExTorque(self,x):
        cmd = 'DcSeCarExT_'
        return getDoubleFromString(self.sendEEFPositionWithFeedback(cmd,x),7)

    def sendEEfPositionGetActualEEFpos(self,x):
        cmd = 'DcSeCarEEfP_'
        return getDoubleFromString(self.sendEEFPositionWithFeedback(cmd,x),6)

    def sendEEfPositionGetActualJpos(self,x):
        cmd = 'DcSeCarJP_'
        return getDoubleFromString(self.sendEEFPositionWithFeedback(cmd,x),7)

    def sendEEfPositionGetEEF_Force_rel_EEF(self,x):
        cmd = 'DcSeCarEEfP_'
        return getDoubleFromString(self.sendEEFPositionWithFeedback(cmd,x),6)
    
    def sendEEfPositionMTorque(self,x):
        cmd = 'DcSeCarMT_'
        return getDoubleFromString(self.sendEEFPositionWithFeedback(cmd,x),7)

    # EEF command utility function    
    def sendEEFPositionWithFeedback(self,cmd,x):
        if(len(x)!=6):
            print('Error in sender function [sendEEFPositionWithFeedback]')
            print('EEF position shall be an array of 6 elements')
            return
        num=1000 # micro-meter accuracy, limit the number of digits in Cartesian position
        buff = cmd
        counter=0
        while counter<6:
            if counter<3:
                buff = buff + str(math.ceil(x[counter]*num)/num)
            else:
                buff = buff + str(x[counter])
            buff = buff + '_'            
            counter=counter+1
        buff = buff + '\n'
        return self.send(buff)
        
    # Joint space functions
    def sendJointsPositions(self,x):
        if(len(x)!=7):
            print('Error in sender function [sendJointsPositions]')
            print('Joint positions shall be an array of 7 elements')
            return
        num=10000
        buff = 'jp_'
        counter=0
        while counter<7:
            buff = buff + str(math.ceil(x[counter]*num)/num)
            buff = buff + '_'            
            counter=counter+1
        buff = buff + '\n'
        self.send(buff)
        
    def sendJointsPositionsGetMTorque(self,x):
        if(len(x)!=7):
            print('Error in sender function [sendJointsPositionsGetMTorque]')
            print('Joint positions shall be an array of 7 elements')
            return
        num=10000
        buff = 'jpMT_'
        counter=0
        while counter<7:
            buff = buff + str(math.ceil(x[counter]*num)/num)
            buff = buff + '_'            
            counter=counter+1
        buff = buff + '\n'
        return getDoubleFromString(self.send(buff),7)

    def sendJointsPositionsGetActualEEFpos(self,x):
        if(len(x)!=7):
            print('Error in sender function [sendJointsPositionsGetExTorque]')
            print('Joint positions shall be an array of 7 elements')
            return
        num=10000
        buff = 'jpEEfP_'
        counter=0
        while counter<7:
            buff = buff + str(math.ceil(x[counter]*num)/num)
            buff = buff + '_'            
            counter=counter+1
        buff = buff + '\n'
        return getDoubleFromString(self.send(buff),6)

    def sendJointsPositionsGetEEF_Force_rel_EEF(self,x):
        if(len(x)!=7):
            print('Error in sender function [sendJointsPositionsGetExTorque]')
            print('Joint positions shall be an array of 7 elements')
            return
        num=10000
        buff = 'DcSeCarEEfFrelEEF_'
        counter=0
        while counter<7:
            buff = buff + str(math.ceil(x[counter]*num)/num)
            buff = buff + '_'            
            counter=counter+1
        buff = buff + '\n'
        return getDoubleFromString(self.send(buff),6)
        
    def sendJointsPositionsGetExTorque(self,x):
        if(len(x)!=7):
            print('Error in sender function [sendJointsPositionsGetExTorque]')
            print('Joint positions shall be an array of 7 elements')
            return
        num=10000
        buff = 'jpExT_'
        counter=0
        while counter<7:
            buff = buff + str(math.ceil(x[counter]*num)/num)
            buff = buff + '_'            
            counter=counter+1
        buff = buff + '\n'
        return getDoubleFromString(self.send(buff),7)
        
    def sendJointsPositionsGetActualJpos(self,x):
        if(len(x)!=7):
            print('Error in sender function [sendJointsPositionsGetActualJpos]')
            print('Joint positions shall be an array of 7 elements')
            return
        num=10000
        buff = 'jpJP_'
        counter=0
        while counter<7:
            buff = buff + str(math.ceil(x[counter]*num)/num)
            buff = buff + '_'            
            counter=counter+1
        buff = buff + '\n'
        return getDoubleFromString(self.send(buff),7)

    # Functions for arc motion
    def sendCirc1FramePos(self,fpos):
        if(len(fpos)!=6):
            print('Error in sender function [sendCirc1FramePos]')
            print('Frame cooridnate is an array of 6 elements [x,y,z,alpha,beta,gamma] ')
            return
        num=10000
        buff = 'cArtixanPositionCirc1_'
        counter=0
        while counter<6:
            buff = buff + str(math.ceil(x[counter]*num)/num)
            buff = buff + '_'            
            counter=counter+1
        buff = buff + '\n'
        self.send(buff)
        
    def sendCirc2FramePos(self,fpos):
        if(len(fpos)!=6):
            print('Error in sender function [sendCirc2FramePos]')
            print('Frame cooridnate is an array of 6 elements [x,y,z,alpha,beta,gamma] ')
            return
        num=10000
        buff = 'cArtixanPositionCirc2_'
        counter=0
        while counter<6:
            buff = buff + str(math.ceil(x[counter]*num)/num)
            buff = buff + '_'            
            counter=counter+1
        buff = buff + '\n'
        self.send(buff)
        


    
