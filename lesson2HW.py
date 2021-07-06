# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
m = (int(input("input your math score: ")))
e = (int(input("input your English score: ")))
score = (m + e)
if(score >= 180):
    print("有獎品!")
elif(score < 120):
    print("要受罰!!")
else:
    print("再加油!")
