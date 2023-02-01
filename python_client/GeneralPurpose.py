# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:45:29 2018

@author: Mohammad SAFEEA
"""

import sys
import numpy as np


alfa = [0, -np.pi / 2, np.pi / 2, np.pi / 2, -np.pi / 2, -np.pi / 2, np.pi / 2]
# iiwa 7 R 800
# d = [0.34, 0.0, 0.4, 0.0, 0.4, 0.0, 0.126]
# iiwa 14 R 820
d = [0.36, 0.0, 0.42, 0.0, 0.4, 0.0, 0.126]


def getDoubleFromString(message, size):
    strVals = message.split("_")
    doubleVals = []
    counter = 0
    for strVal in strVals:
        counter = counter + 1
        if counter > size:
            break
        try:
            x = float(strVal)
            doubleVals.append(x)
        except:
            print('can not convert the following variable to float')
            print(strVal)
            sys.stdout.flush()

    return doubleVals


def directKinematics(q):
    if len(q) != 7:
        print('Error in function [directKinematics]')
        print('The size of the joint angles shall be 7')
        return

        T = np.zeros((4, 4, 7))
    T[:, :, 0] = getDHMatrix(alfa[0], q[0], d[0], 0)

    for i in range(1, 7):
        T[:, :, i] = T[:, :, i - 1].dot(getDHMatrix(alfa[i], q[i], d[i], 0))
        T[:, :, i] = normalizeColumns(T[:, :, i])

    if TefTool is not None:
        T[:, :, 6] = T[:, :, 6].dot(TefTool)
        T[:, :, 6] = normalizeColumns(T[:, :, 6])
    return T[:3, 3, 6]


def getDHMatrix(alfa, theta, d, a):
    T = np.zeros((4, 4))

    calpha = np.cos(alfa)
    sinalpha = np.sin(alfa)
    coshteta = np.cos(theta)
    sintheta = np.sin(theta)

    T[0, 0] = coshteta
    T[1, 0] = sintheta * calpha
    T[2, 0] = sintheta * sinalpha

    T[0, 1] = -sintheta
    T[1, 1] = coshteta * calpha
    T[2, 1] = coshteta * sinalpha

    T[1, 2] = -sinalpha
    T[2, 2] = calpha

    T[0, 3] = a
    T[1, 3] = -sinalpha * d
    T[2, 3] = calpha * d
    T[3, 3] = 1

    return T


def normalizeColumns(T):
    r = np.zeros((4, 3))
    for j in range(3):
        r[:3, j] = T[:3, j] / (np.linalg.norm(T[:3, j]) + 1e-6)
    return np.concatenate([r, T[:, 3:4]], axis=1)
