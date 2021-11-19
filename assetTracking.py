import json
from logging import error, exception
from os import path
from app_logging import AppLogger

class AssetTracker:
    def __init__(self, nftTraits):
        self.newTraits = nftTraits
        self.fileName = "nftTracking/NFT_tracking.json"
        self.appLogger = AppLogger()


    def checkNFTUniqueness(self, current_traits: dict, new_traits: dict) -> bool:
        # retrieve json file, and check new traits against all traits in file
        for key in current_traits:
            if current_traits["traits_ID"] == new_traits["traits_ID"]:
                return False
        # No match was found, so the traits are unique ...
        # return True
        return True
       
    def checkNFT_IDUniqueness(self, current_ids, new_id):
        test_3 = current_ids
        test_4 = new_id

        stopPoint = 2

    def saveNFTTraits(self):
        # Check if new NFT's traits are unique
        # if unique save new traits to json file
        try:
            #test3 = self.newTraits.append()
            # Convert dictionary to json object
            currentData = self.newTraits
            newData = self.newTraits
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print(self.newTraits.update(newData['NFT_Traits']))
            
             
            return True
        except FileNotFoundError:
            print("File was not found: {0}".format(self.fileName))
            return False
        # else return false, and run again to get unique traits
        
    def getNFTdata(self):
        pass

    def saveNFTdata(self):
        try:
            if path.exists(self.fileName):
                with open(self.fileName, 'r') as file:
                    previous_json = json.load(file)
                    # Make sure the NFT id is unique ...
                    # and the traits_id is unique
                    # if self.checkNFTUniqueness(previous_json, self.newTraits):
                    #     nfts = previous_json + self.newTraits
                    # else:
                    #     # The 
                    #     return
                    nfts = previous_json + self.newTraits

                with open(self.fileName, 'w') as file:
                    json.dump(nfts, file, indent=4)
            return True
        except Exception as err:
            exception_message = "Problem accessing file: {}".format(str(err))
            print(exception_message)
            self.appLogger.log_errors(exception_message)
            self.appLogger.log_info("Attempting to write to file")
            # The exception was thrown due to trying to read an empty file
            # There is no data to append to, so save the first entry
            with open(self.fileName, 'w') as file:
                    json.dump(self.newTraits, file, indent=4)
            return True

