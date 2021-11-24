import unittest
from assetTracking import *
from random import randint
import logging

from dudeBro import DudeBro

class TestDudeBro(unittest.TestCase):
    
   
    def setUp(self):
        
        self.fileName = "nftTracking/NFT_tracking_unit_tests.json"
        self.testTraitsList = [
            {
                "NFT_ID":1, 
                "face":randint(1, 13),
                "body":randint(1, 20),
                "eyebrows":randint(1, 13),
                "eyes": randint(1, 16),
                "facialhair":randint(0, 3),
                "glasses":randint(0, 20),
                "hair": randint(1, 21),
                "hat" : randint(0, 27),
                "mouth": randint(1, 12),
                "smoke":randint(0, 3),
                "traits_ID":None
                
            }]

        self.dude_bro_instance = DudeBro(0)
    
    # def test_get_NFT_data(self):
    #    nftData = self.dude_bro_instance.get_NFT_data(self.testTraitsList, fileName=self.fileName)
    #    self.assertIsNotNone(nftData)


    def test_create_trait_id(self):
       new_trait_id = self.dude_bro_instance.create_trait_id(self.testTraitsList)
       self.testTraitsList[0]["traits_ID"] = new_trait_id
       self.assertIsNotNone(self.testTraitsList[0]["traits_ID"])




if __name__ == '__main__':
    unittest.main()