from PIL import Image
import numpy as np
import os as os
import json as json
from pathlib import Path
import requests
from helpers import *


cwd = os.getcwd()
ASSETFOLDER = "%s\\Assets\\"%(cwd)

class DudeBro:
    
    
    TOTAL = 1100
    def __init__(self, itr):
        self.id = itr
        self.generate_dude_bro(itr)
        
    
    def generate_dude_bro(self, itr):
        body = generateRandomNumber(1, 20)
        face = generateRandomNumber(1, 13)
        eyes = generateRandomNumber(1, 16)
        eyebrows = generateRandomNumber(1, 13)
        mouth = generateRandomNumber(1, 12)
        hair = generateRandomNumber(1, 21)
        
        # OPTIONAL - higher range equals increase randomness, less likely to align with exisiting feature
        facialHair = generateRandomNumber(0, 3)
        smoke = generateRandomNumber(0, 3)
        hat = generateRandomNumber(0, 27)
        glasses = generateRandomNumber(0, 20)
        
        # Feature Dict
        bodyDict = createBodyDict()
        faceDict = createFaceDict()
        eyeDict = createEyeDict()
        eyeBrowDict = createEyebrowsDict()
        mouthDict = createMouthDict()
        hairDict = createHatDict()
        facialHairDict = createFacialHairDict()
        smokeDict = createSmokeDict()
        hatDict = createHatDict()
        glassesDict = createGlassesDict()
        
        
        # Open Required pngs (Body, Eyes, Mouth)
        img0 = Image.open(ASSETFOLDER + "Face/" + str(face) + ".png")
        img1 = Image.open(ASSETFOLDER + "Body/" + str(body) + ".png")
        img2 = Image.open(ASSETFOLDER + "Eyes/" + str(eyes) + ".png")
        img3 = Image.open(ASSETFOLDER + "Mouth/" + str(mouth) + ".png")
        img4 = Image.open(ASSETFOLDER + "Hair/" + str(hair) + ".png")
        img5 = Image.open(ASSETFOLDER + "Eyebrows/" + str(eyebrows) + ".png")
        
        # Paste Required PNGs
        img0.paste(img1, (0,0), img1)
        img0.paste(img2, (0,0), img2)
        img0.paste(img3, (0,0), img3)
        img0.paste(img4, (0,0), img4)
        img0.paste(img5, (0,0), img5)
        
        # Open and paste Optional PNGs
        if(0 < facialHair <= 3):
            img6 = Image.open(ASSETFOLDER + "FacialHair/" + str(facialHair) + ".png")
            img0.paste(img6, (0,0), img6)
            
        if (0 < smoke <= 3):
            img7 = Image.open(ASSETFOLDER + "Cigarette/" + str(smoke) + ".png")
            img0.paste(img7, (0,0), img7)
        
        if (0 < hat <= 27):
            img8 = Image.open(ASSETFOLDER + "Hat/" + str(hat) + ".png")
            img0.paste(img8, (0,0), img8)
        
        if (0 < glasses <= 20):
            img9 = Image.open(ASSETFOLDER + "Glasses/" + str(glasses) + ".png")
            img0.paste(img9, (0,0), img9)
        
        
        # Create and save
        folder = ASSETFOLDER + "DudeBros/"
        if not os.path.isdir(folder):
            os.mkdir(folder)
        
        img0.save(folder + str(generateRandomNumber(1, 5000)) + '.png', "PNG")
        