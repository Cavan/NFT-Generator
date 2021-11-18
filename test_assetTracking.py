import unittest
from assetTracking import *
from random import randint
import logging

class TestAssetTracker(unittest.TestCase):
    
   
    def setUp(self):
        
        # Store new ID
        self.nftID = randint(1000, 5000)
        self.unique_nftID = randint(1000, 5000)
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
        self.assertFalse(self.testTracker.checkNFTUniqueness(self.testTraitsList, self.testTraitsList))
    
    def test_checkNFTUniquenessPasses(self):
        self.assertTrue(self.testTracker.checkNFTUniqueness(self.testTraitsList, self.testTraitsList))

    def test_NFT_id_UniquesnessFails(self):
        pass

    def test_NFT_id_UniquenessPasses(self):
        pass 

    def test_saveNFTdata(self):
        resultValue = self.testTracker.saveNFTdata()
        self.assertTrue(resultValue)

    

if __name__ == '__main__':
    unittest.main()