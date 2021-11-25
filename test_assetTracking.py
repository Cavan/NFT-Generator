import unittest
from assetTracking import *
from random import randint
import logging

class TestAssetTracker(unittest.TestCase):
    
   
    def setUp(self):
        
        self.fileName = "nftTracking/NFT_tracking_unit_tests.json"
        nft_traits = []
        # Store new ID
        # Open nft data
        self.testTracker = AssetTracker(self.fileName)
        self.stored_NFT_data = self.get_NFT_data(nft_traits)
        if self.stored_NFT_data == None:
            self.nftID = 1
        else:
            max_nft_id = self.testTracker.get_max_NFT_id(self.stored_NFT_data)
            max_nft_id += 1
            self.nftID = max_nft_id
            

        #self.nftID = randint(1, 5000)
        self.unique_nftID = randint(1000, 5000)
        self.unique_traitsID = randint(1000000000000, 7000000000000)
        self.testTraitsList = [
            {
                "NFT_ID":self.nftID, 
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
        #self.testTracker = AssetTracker(self.testTraitsList)
        self.testTracker.set_new_traits(self.testTraitsList)



    def tearDown(self):
        pass
    
    def test_checkNFTUniquenessFails(self):
        numberOfEntries = len(self.stored_NFT_data)
        rndIndex = randint(0, numberOfEntries)
        if numberOfEntries == 1:
            rndIndex = 0
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
        if numberOfEntries == 1:
            randomIndex = 0
        nonUniqueID = self.stored_NFT_data[randomIndex]["NFT_ID"]
        result = self.testTracker.checkNFT_IDUniqueness(self.stored_NFT_data, nonUniqueID)
        self.assertFalse(result)

    def test_NFT_id_UniquenessPasses(self):

        result = self.testTracker.checkNFT_IDUniqueness(self.stored_NFT_data,self.unique_nftID)
        self.assertTrue(result) 

    
    def test_saveNFTdata(self):
        resultValue = self.testTracker.saveNFTdata(self.fileName)
        self.assertTrue(resultValue)

    def test_get_max_NFT_id(self):
        nft_data = self.get_NFT_data(self.testTraitsList)
        test_value = self.testTracker.get_max_NFT_id(nft_data)
        self.assertIsNotNone(test_value)
    




    # Helper methods
    def get_NFT_data(self, newTraits):
        try:
            if path.exists(self.fileName):
                with open(self.fileName, 'r') as file:
                    previous_json = json.load(file)
            else:
                previous_json = [
            {
                "NFT_ID":0,
                "face":0,
                "body":0,
                "eyebrows":0,
                "eyes": 0,
                "facialhair":0,
                "glasses":0,
                "hair": 0,
                "hat" : 0,
                "mouth": 0,
                "smoke":0,
                "traits_ID":None
                
            }]
            return previous_json
        except Exception as err:
            exception_message = "Problem accessing file: {}".format(str(err))
            print(exception_message)
            # The exception was thrown due to trying to read an empty file
            # There is no data to append to, so save the first entry
            # with open(self.fileName, 'w') as file:
            #         json.dump(newTraits, file, indent=4)
            return None



if __name__ == '__main__':
    unittest.main()