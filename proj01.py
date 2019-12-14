# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 18:37:17 2017

@author: Ashton
"""
#####################################################################
#   CSE 231 Project 1
#       
#   Algorithm    
#       Prompt for a distance in rods
#       Convert distace input from string to float 
#       Convert rods to meters, feet, miles, furlongs, and walk time
#       Display conversions
#####################################################################

dist_rods_str = input ( "Input a distance in rods: " )
#Prompts user to input a distance
dist_rods_flt = float ( dist_rods_str )
#Converts user's input from a string to a float
print ( " You input " , dist_rods_flt , " rods. " )
#Displays what the user input
dist_meter = dist_rods_flt * 5.0292
#Converts from rods to meters
dist_ft = dist_meter / .3048
#Converts from rods, to meters, to feet
dist_miles = dist_meter / 1609.34
#Converts from rods, to meters, to miles
dist_furlongs = dist_rods_flt / 40 
#Converts from rods to furlongs
time_mins = dist_miles / ( 3.1 / 60 )
#Converts from rods, to meters, to miles, to minutes
print ( "" )
#Leaves space between the input and conversions
print ( " Conversions: " )
#Displays the header: "Conversions: "
print ( " Distance in meters is: " , dist_meter )  
#Displays distance in meters
print ( " Distance in feet is: " , dist_ft )  
#Displays distance in feet
print ( " Distance in miles is: " , dist_miles )
#Displays distance in miles
print ( " Distance in furlongs is: " , dist_furlongs )
#Displays distance in furlongs
print ( " Walk time in minutes is: " , time_mins )
#Displays walk time in minutes