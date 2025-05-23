import os
import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgBackground=cv2.imread("resources/Backgroud.png")
folderPathModes = "resources/Modes"
listImgModesPath = os.listdir(folderPathModes) 
 
listImgModes = []

for imgModePath in listImgModesPath:
    fullPath = os.path.join(folderPathModes, imgModePath)
    img = cv2.imread(fullPath)
    listImgModes.append(img)

folderpathIcons="resources/Icons"
listImgIconsPath=os.listdir(folderpathIcons)

listImgIcons = []

for imgIconspath in listImgIconsPath:
    fullpath=os.path.join(folderpathIcons,imgIconspath)
    img = cv2.imread(fullpath)
    listImgIcons.append(img)

modetype = 0
selection = -1
counter = 0
selectionspeed = 7

detector = HandDetector(detectionCon = 0.8, maxHands = 1)  

modepositions = [(1136, 196), (1000, 384), (1136, 581)]

counterpause = 0

selectionList = [-1,-1,-1]

while True:
    success,img = cap.read()
    hands,img = detector.findHands(img)
    imgBackground[0:480, 0:640] = img
    imgBackground[0:720, 847:1280] = listImgModes[modeType]
    
    imgBackground = cv2.imread("resources/Background.png")
    if imgBackground is None:
        raise FileNotFoundError("Background image not found. Check the file path and spelling.")

       
    if hands and counterPause == 0 and modeType < 3:
        hand1 = hands[0]  
        fingers1 = detector.fingersUp(hand1)  
        print(fingers1)
        
        if fingers1 == [0, 1, 0, 0, 0]: 
            if selection != 1:
                counter = 1 
            selection = 1
            
        elif fingers1 == [0, 1, 1, 0, 0]:  
            if selection != 2:
                counter = 1
            selection = 2
            
        elif fingers1 == [0, 1, 1, 1, 0]: 
            if selection != 3:
                counter = 1
            selection = 3
            
        else:
            selection = -1 
            counter = 0
 
        
        if counter > 0:
            counter += 1
            
            cv2.ellipse(imgBackground,modePositions[selection - 1],(103, 103), 0, 0, counter * selectionSpeed,(0, 255, 0), 20)

            if counter * selectionSpeed > 360:
                selectionList[modeType] = selection    
                modeType += 1                           
                counter = 0                             
                selection = -1                         
                counterPause = 1                 
                
    
    if counterPause > 0:
        counterPause += 1
        if counterPause > 60:  
            counterPause = 0

    
    if selectionList[0] != -1:
        imgBackground[636:636 + 65, 133:133 + 65] = listImgIcons[selectionList[0] - 1]  
    if selectionList[1] != -1:
        imgBackground[636:636 + 65, 340:340 + 65] = listImgIcons[2 + selectionList[1]]  
    if selectionList[2] != -1:
        imgBackground[636:636 + 65, 542:542 + 65] = listImgIcons[5 + selectionList[2]]

    
    cv2.imshow("Background", imgBackground)
    cv2.waitKey(1)

