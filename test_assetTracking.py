import unittest
from assetTracking import *
from random import randint
import logging

class TestAssetTracker(unittest.TestCase):
    
   
    def setUp(self):
        
        self.testTraitsList = [
            {
                "NFT_ID":randint(1000, 5000), 
                "face":6,
                "body":3,
                "eyebrows":4,
                "eyes": 12,
                "facialhair":2,
                "glasses":11,
                "hair": 17,
                "hat" : 20,
                "mouth": 5
            }]
            
        # Create a class instance of AssetTracker
        self.testTracker = AssetTracker(self.testTraitsList)
        

    def tearDown(self):
        pass
    
    def test_checkNFTUniqueness(self):
        self.assertTrue(self.testTracker.checkNFTUniqueness())

    def test_saveNFTTraits(self):
        resultValue = self.testTracker.saveNFTTraits()
        self.assertTrue(resultValue)

    def test_saveNFTdata(self):
        resultValue = self.testTracker.saveNFTdata()
        self.assertTrue(resultValue)

    

if __name__ == '__main__':
    unittest.main()