#!/usr/bin/python3

import pickle       #Will Use to condense image files
import cv2          #Will be needed for image manipulation
import os           #Will need to navigate linux file system
import xlsxwriter   #Record data in Excel

class memberData:
    date= ""        #Autofill
    timestamp= ""   #Autofill
    level= ""       #More complicated
    def __init__(self, lastName, firstName, netID):
        '''
        '''
        self.lastName = lastName
        self.firstName = firstName
        self.netID = netID

    def updateMemberInfo():
        '''
        '''
        pass

def main():
    '''
    Description:

    Parameters: 

    Preconditions:

    Returns: 
    '''
    defaultMenu()

def defaultMenu():
    '''
    '''
    print("Welcome to Automated Attendance beta1.0!\n")
    print("If you have registered with this program before and would like to scan \
        your Cornell Student ID, enter 1.")
    print("If you have registered with this program before and would like to login \
        manually, enter 2.")
    print("If you have never used this program before, enter 3.")
    print("To shutdown the program, enter 4.")
    #print("Please enter your choice below:\t")
    usrSelect = input("Please enter your choice below:\t")
    if usrSelect == "1":
        pass
    elif usrSelect == "2":
        signUp()
    elif usrSelect == "3":
        pass
    elif usrSelect == "4":
        print("Shutting down program now!")
        exit()
    else:
        print("Invalid input!")
        print("Please be sure to enter 1, 2, or 3.\n")
        defaultMenu()

def signUp():
    '''
    '''
    print("\nIn order to register with this program, please enter the following information:")
    lName = input("Enter your LAST NAME as it is printed on your Cornell Student ID:\t")
    fName = input("Enter your FIRST NAME as it is printed on your Cornell Student ID:\t")
    netid = input("Enter your NETID:\t")
    newMem = memberData(lName, fName, netid)
    print("\nInformation entered: {0} {1} {2}".format(newMem.firstName, newMem.lastName, newMem.netID))

#####################
main()
#####################