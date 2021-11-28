from PIL import Image
import numpy as np
import os as os
import json as json
from pathlib import Path
import requests
from helpers import *
from assetTracking import AssetTracker
from brownie import (
    network,
    accounts,
    config,
)
cwd = os.getcwd()
ASSETFOLDER = "%s\\Assets\\"%(cwd)

class DudeBro:
    
    
    TOTAL = 1100
    def __init__(self, itr):
        self.id = itr
        self.NFT_ID = 0
        self.m_data = self.generate_meta_data(self.NFT_ID) 
        self.nft_tracker_fileName = "nftTracking/DudeBros_NFT_tracking.json"
        self.assetTracker = AssetTracker(self.nft_tracker_fileName)
        if itr > 0 :
            self.generate_dude_bro(itr)
            
    
    def generate_meta_data(self, token_id):
        dude_bro_metadata = sample_metadata.metadata_template
        dude_bro_metadata["name"] = str(token_id)
        dude_bro_metadata["description"] = "DudeBros is a generative art project"
        dude_bro_metadata["image"] = ''
        dude_bro_metadata["background_color"] = '0F7CB3'
        # Image will be added with attributes after the creation of DudeBro
        dude_bro_metadata["attributes"] = []
        return dude_bro_metadata




    def generate_dude_bro(self, itr):
        isNFT_unique = False
        storred_NFT_data = self.assetTracker.getNFTdata()
        # Assign an NFT numeric id that will be used for the filename when saving
        if storred_NFT_data == None:
            self.NFT_ID = 1
        else:
            # find the highest id number, and increment it by 1 ...
            # this will be the new NFT id
            max_nft_id = self.assetTracker.get_max_NFT_id(storred_NFT_data)
            max_nft_id += 1
            self.NFT_ID = max_nft_id

        # Create a while loop that will check the NFT ID ...
        # and continue until a unique value is created.
        while isNFT_unique != True :
            body = generateRandomNumber(1, 20)
            face = generateRandomNumber(1, 6)
            eyes = generateRandomNumber(1, 16)
            eyebrows = generateRandomNumber(1, 13)
            mouth = generateRandomNumber(1, 12)
            hair = generateRandomNumber(1, 21)
            
            # OPTIONAL - higher range equals increase randomness, less likely to align with exisiting feature
            facialHair = generateRandomNumber(0, 3)
            smoke = generateRandomNumber(0, 3)
            hat = generateRandomNumber(0, 27)
            glasses = generateRandomNumber(0, 20)
            
            # Add traits to dictionary 
            NFT_features = [
                {
                    "NFT_ID":self.NFT_ID, 
                    "face":face,
                    "body":body,
                    "eyebrows":eyebrows,
                    "eyes": eyes,
                    "facialhair":facialHair,
                    "glasses":glasses,
                    "hair": hair,
                    "hat" : hat,
                    "mouth": mouth,
                    "traits_ID":None
                }]

            new_NFI_trait_ID = self.create_trait_id(NFT_features)
            # Assign the new trait id before checking its uniqueness
            NFT_features[0]["traits_ID"] = new_NFI_trait_ID
            isNFT_unique = self.assetTracker.checkNFTUniqueness(storred_NFT_data, NFT_features)

        # Set the new traits for the asset tracker
        self.assetTracker.set_new_traits(NFT_features)
        # The NFT is unique so save the traits to file using the AssetTracker class
        self.assetTracker.saveNFTdata(self.nft_tracker_fileName)


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
        self.m_data['attributes'].append(
            {
                'trait-type':'Skin Shade',
                'value': faceDict[face]
            })
        
        self.m_data['attributes'].append(
            {
                'trait-type':'Body Color',
                'value': bodyDict[body]
            })
        self.m_data['attributes'].append(
            {
                'trait-type':'Eye Color',
                'value': eyeDict[eyes]
            })
        self.m_data['attributes'].append(
            {
                'trait-type':'Mouth / Lips',
                'value': mouthDict[mouth]
            })
        self.m_data['attributes'].append(
            {
                'trait-type':'Hair Color',
                'value': hairDict[hair]
            })
        self.m_data['attributes'].append(
            {
                'trait-type':'Eyebrows',
                'value': eyeBrowDict[eyebrows]
            })



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
            self.m_data['attributes'].append(
            {
                'trait-type':'Facial Hair',
                'value': facialHairDict[facialHair]
            })
            
        if (0 < smoke <= 4):
            img7 = Image.open(ASSETFOLDER + "Cigarette/" + str(smoke) + ".png")
            img0.paste(img7, (0,0), img7)
            self.m_data['attributes'].append(
            {
                'trait-type':'Dirty Habit',
                'value': smokeDict[smoke]
            })
        
        if (0 < hat <= 27):
            img8 = Image.open(ASSETFOLDER + "Hat/" + str(hat) + ".png")
            img0.paste(img8, (0,0), img8)
            self.m_data['attributes'].append(
            {
                'trait-type':'Headwear',
                'value': hatDict[hat]
            })
        
        if (0 < glasses <= 20):
            img9 = Image.open(ASSETFOLDER + "Glasses/" + str(glasses) + ".png")
            img0.paste(img9, (0,0), img9)
            self.m_data['attributes'].append(
            {
                'trait-type':'Eyewear',
                'value': glassesDict[glasses]
            })
        
        # Create and save
        folder = ASSETFOLDER + "DudeBros/"
        if not os.path.isdir(folder):
            os.mkdir(folder)
        
        # Check if file name already exists
        # Get complete list of files
        # Take the length and increment by 1

        # Saving file
        print("Saving file in progress")
        img0.save(folder + 'DudeBro_' + str(self.NFT_ID) + '.png', "PNG")


    def create_trait_id(self, newTraits):
        # We are going to combine each trait value into ...
        # a trait_ID, before each NFT is generated we'll check to make sure
        # we're not producing an NFT with the same traits.
        temp_traits_id = ''
        trait_dict = newTraits[0]
        for key in trait_dict:
            if key != "NFT_ID" and key != "traits_ID":   
                temp_traits_id += str(trait_dict[key])
             
        # Assign the traits id to be stored in the json file
        return int(temp_traits_id)