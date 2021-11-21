import unittest
from assetTracking import *
from random import randint
import logging

class TestAssetTracker(unittest.TestCase):
    
   
    def setUp(self):
        
        self.fileName = "nftTracking/NFT_tracking.json"

        # Store new ID
        self.nftID = randint(1000, 5000)
        self.unique_nftID = randint(1000, 5000)
        self.unique_traitsID = randint(1000000000000, 7000000000000)
        self.testTraitsList = [
            {
                "NFT_ID":self.nftID, 
                "face":6,
                "body":3,
                "eyebrows":4,
                "eyes": 12,
                "facialhair":2,
                "glasses":11,
                "hair": 17,
                "hat" : 20,
                "mouth": 5,
                "traits_ID":None
                
            }]
        self.stored_NFT_data = self.get_NFT_data(self.testTraitsList)
        
        # We are going to combine each trait value into ...
        # a trait_ID, before each NFT is generated we'll check to make sure
        # we're not producing an NFT with the same traits.
        temp_traits_id = ''
        trait_dict = self.testTraitsList[0]
        for key in trait_dict:
            if key != "NFT_ID" and key != "traits_ID":   
                temp_traits_id += str(trait_dict[key])
             
        # Assign the traits id to be stored in the json file
        self.testTraitsList[0]['traits_ID'] = int(temp_traits_id)
        #self.testTraitsList['traits_ID'] = int(temp_traits_id)
        # Create a class instance of AssetTracker        
        self.testTracker = AssetTracker(self.testTraitsList)



    def tearDown(self):
        pass
    
    def test_checkNFTUniquenessFails(self):
        numberOfEntries = len(self.stored_NFT_data)
        rndIndex = randint(0, numberOfEntries)
        traitsDict = self.stored_NFT_data.copy()
        result = self.testTracker.checkNFTUniqueness(self.stored_NFT_data, self.stored_NFT_data[rndIndex])
        self.assertFalse(result)
    
    def test_checkNFTUniquenessPasses(self):
        unique_traits_dict = self.testTraitsList[0].copy()
        unique_traits_dict["traits_ID"] = self.unique_traitsID

        result = self.testTracker.checkNFTUniqueness(self.stored_NFT_data, unique_traits_dict)
        self.assertTrue(result)

    def test_NFT_id_UniquesnessFails(self):
        numberOfEntries = len(self.stored_NFT_data)
        randomIndex = randint(0, numberOfEntries)
        nonUniqueID = self.stored_NFT_data[randomIndex]["NFT_ID"]
        result = self.testTracker.checkNFT_IDUniqueness(self.stored_NFT_data, nonUniqueID)
        self.assertFalse(result)

    def test_NFT_id_UniquenessPasses(self):

        result = self.testTracker.checkNFT_IDUniqueness(self.stored_NFT_data,self.unique_nftID)
        self.assertTrue(result) 

    




    # Helper methods
    
    def test_saveNFTdata(self):
        resultValue = self.testTracker.saveNFTdata()
        self.assertTrue(resultValue)

    def get_NFT_data(self, newTraits):
        try:
            if path.exists(self.fileName):
                with open(self.fileName, 'r') as file:
                    previous_json = json.load(file)
                    
            return previous_json
        except Exception as err:
            exception_message = "Problem accessing file: {}".format(str(err))
            print(exception_message)
            # The exception was thrown due to trying to read an empty file
            # There is no data to append to, so save the first entry
            with open(self.fileName, 'w') as file:
                    json.dump(newTraits, file, indent=4)
            return newTraits



if __name__ == '__main__':
    unittest.main()