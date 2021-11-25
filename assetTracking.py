import json
from logging import error, exception
from os import path
import os as os
from app_logging import AppLogger

class AssetTracker:
    def __init__(self, fileName):
        self.newTraits = None
        self.fileName = fileName
        self.appLogger = AppLogger()


    def set_new_traits(self, new_traits):
        self.newTraits = new_traits


    def checkNFTUniqueness(self, current_traits, new_traits):
        try:
            # If the NFT_ID equals 1 then this is the first NFT in the collection, ...
            # and the traits_ID will be unique so return True
            if new_traits[0]["NFT_ID"] == 1:
                self.appLogger.log_info("First NFT in the collection is being created")
                return True
            indxCounter = 0
            # retrieve json file, and check new traits against all traits in file
            for key in current_traits:
                if current_traits[indxCounter]["traits_ID"] == new_traits[0]["traits_ID"]:
                    self.appLogger.log_warnings("NFT is not unique, Re-Generating")
                    print("NFT is not unique, Re-Generating")
                    return False
                indxCounter += 1
            # No match was found, so the traits are unique ...
            # return True
            return True
        except Exception as err:
            exception_message = "Problem checking NFT uniqueness, program cannot continue: {}".format(str(err))
            self.appLogger.log_errors(exception_message)
            raise Exception("Program cannot continue, need to fix this exception")
       
    def checkNFT_IDUniqueness(self, current_ids, new_id):
        indxCounter = 0
        for index in current_ids:
            if current_ids[indxCounter]["NFT_ID"] == new_id:
                return False
            indxCounter += 1
        # No match was found so the NFT id is unique
        return True

        

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
        try:
            if os.path.exists(self.fileName):
                with open(self.fileName, 'r') as file:
                    previous_json = json.load(file)
                self.appLogger.log_info("Successfully retrieved NFT data")
            else:
                previous_json = None

            return previous_json
        except Exception as err:
            exception_message = "Problem accessing file: {}".format(str(err))
            self.appLogger.log_errors(exception_message)
            print(exception_message)
            # The exception was thrown due to trying to read an empty file
            # There is no data to append to, so save the first entry
            
            return None  

    def saveNFTdata(self, fileName):
        try:
            if path.exists(fileName):
                with open(fileName, 'r') as file:
                    previous_json = json.load(file)
                    # Make sure the NFT id is unique ...
                    # and the traits_id is unique
                    # if self.checkNFTUniqueness(previous_json, self.newTraits):
                    #     nfts = previous_json + self.newTraits
                    # else:
                    #     # The 
                    #     return
                    if previous_json != None:
                        nfts = previous_json + self.newTraits
                    else:
                        nfts = self.newTraits

                with open(fileName, 'w') as file:
                    json.dump(nfts, file, indent=4)
            else:
                with open(fileName, 'w') as file:
                    json.dump(self.newTraits, file, indent=4)

            self.appLogger.log_info("Successfully saved new NFT data")        
            return True
        except Exception as err:
            exception_message = "Problem accessing file: {}".format(str(err))
            print(exception_message)
            self.appLogger.log_errors(exception_message)
            self.appLogger.log_info("Attempting to write to file")
            # The exception was thrown due to trying to read an empty file
            # There is no data to append to, so save the first entry
            with open(fileName, 'w') as file:
                    json.dump(self.newTraits, file, indent=4)
            return True

    # sort the NFTs and return the highest value
    def get_max_NFT_id(self, nft_data):
        
        nft_ids_list = []
        sorted_list = []
        index_counter = 0
        for id in nft_data:
            nft_ids_list.append(nft_data[index_counter]["NFT_ID"])
            index_counter += 1

        max_id = max(nft_ids_list)

        return max_id
        

        