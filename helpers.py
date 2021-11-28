
import numpy as np

def generateRandomNumber(lowIn, highIn):
        rng = np.random.default_rng()
        ranNumberArray = rng.integers(low=lowIn, high=highIn, size=1)
        return int(ranNumberArray[0])


def createBodyDict():
        bodyDict = {
            1: 'Ash Grey Body',
            2: 'Dark Red Body',
            3: 'Dark Grey Body',
            4: 'Yellow Body',
            5: 'Bright Green Body',
            6: 'Black Body',
            7: 'Deep Pink Body',
            8: 'Red Body',
            9: 'Blue Body',
            10: 'Purple Body',
            11: 'Amber Body',
            12: 'Light Grey',
            13: 'Bright Lime Body',
            14: 'Candy Apple Red Body',
            15: 'Cyan Body',
            16: 'Celadon Green Body',
            17: 'Medium Purple Body',
            18: 'Deep Fuchsia Body',
            19: 'Candy Pink Body',
            20: 'Arsenic Body'
        }
        return bodyDict
    
    
    
def createFaceDict():
    faceDict = {
        1: 'Face Shade 1',
        2: 'Face Shade 2',
        3: 'Face Shade 3',
        4: 'Face Shade 4',
        5: 'Face Shade 5',
        6: 'Face Shade 6'
    }
    return faceDict
    
    
def createEyeDict():
    eyeDict ={
         1: 'Black Pupils',
        2: 'Red Pupils',
        3: 'Bright Green Eyes',
        4: 'Red Eyes',
        5: 'White Pupils',
        6: 'Black Eyes',
        7: 'Red Eyes, Black Pupils',
        8: 'Bright Green Eyes, Black Pupils',
        9: 'Pink Pupils',
        10: 'Yellow Pupils',
        11: 'Bright Green Pupils',
        12: 'Sky Blue Pupils',
        13: 'Black Pupils',
        14: 'Black Pupils',
        15: 'Red Pupils',
        16: 'Bright Pink Pupils'
    }
    return eyeDict




def createEyebrowsDict():
    eyebrowDict ={
        1: 'Red Eyebrows',
        2: 'Brown Eyebrows',
        3: 'Arsenic Eyebrows',
        4: 'Bistre Eyebrows',
        5: 'Bright Yellow Eyebrows',
        6: 'Black Eyebrows',
        7: 'Bright Green Eyebrows',
        8: 'Orange Eyebrows',
        9: 'Bistre Eyebrows',
        10: 'Light Blue Eyebrows',
        11: 'Medium Spring Green',
        12: 'Black Bean Eyebrows',
        13: 'Cultured Eyebrows'
    }
    return eyebrowDict


def createMouthDict():
    mouthDict = {
        1: 'Lips Shade 1',
        2: 'Lips Shade 2',
        3: 'Red Lips',
        4: 'Bright Green Lips',
        5: 'Dark Blue Lips',
        6: 'Lime Green Lips',
        7: 'Amber Lips',
        8: 'Blue Lips',
        9: 'Barn Red Lips',
        10: 'White Lips',
        11: 'Fire Red lips',
        12: 'Peach Lips'
    }
    return mouthDict




def createHairDict():
    hairDict = {
        1: 'Brown Shade 1 Hair',
        2: 'Brown Shade 2 Hair',
        3: 'Lime Green Hair',
        4: 'Brown Shade 3 Hair',
        5: 'Arsenic Hair',
        6: 'Steel Hair',
        7: 'Bright Pink Hair',
        8: 'Deep Blue Hair',
        9: 'Yellow Hair',
        10: 'Forest Green Hair',
        11: 'Orange Hair',
        12: 'Fire Red Hair ',
        13: 'Cyan Hair',
        14: 'Light Purple Hair',
        15: 'Grey Hair',
        16: 'Rose Pink Hair',
        17: 'Black Hair',
        18: 'Dark Yellow Hair',
        19: 'Dark Green Hair',
        20: 'Mint Green Hair',
        21: 'Sky Blue Hair'
    }
    return hairDict



def createFacialHairDict():
    facialHairDict = {
        1: 'Moustache Style 1',
        2: 'Goatee',
        3: 'Beard'
    }
    return facialHairDict



def createSmokeDict():
    smokeDict = {
        1: 'Cigarette',
        2: 'Cigarette Pointed Downward',
        3: 'Cigarette Pointed Upward'
    }
    return smokeDict

def createHatDict():
    hatDict = {
        1: 'Red Baseball Cap',
        2: 'Purple Baseball Cap',
        3: 'Green Baseball Cap',
        4: 'Dark Blue Baseball Cap',
        5: 'Yellow Baseball Cap',
        6: 'Cyan Baseball Cap',
        7: 'Blue Baseball Cap',
        8: 'Orange Baseball Cap',
        9: 'Bright Green Baseball Cap',
        10: 'Grey Baseball Cap',
        11: 'Brown Homburg Hat',
        12: 'Black Bandana',
        13: 'Red Bandana',
        14: 'Bright Green Bandana',
        15: 'Blue Bandana',
        16: 'Orange Bandana',
        17: 'Black Homburg Hat',
        18: 'Red Homburg Hat',
        19: 'Green Homburg Hat',
        20: 'Light Brown Homburg Hat',
        21: 'Deep Pink Homburg Hat',
        22: 'Blue Homburg Hat',
        23: 'Dark Grey Homburg Hat',
        24: 'Light Pink Homburg Hat',
        25: 'Dark Brown Homburg Hat',
        26: 'Yellow Homburg Hat',
        27: 'Light Grey Homburg Hat'
    }
    return hatDict


def createGlassesDict():
    glassesDict = {
        1: 'Black Eye Patch',
        2: 'Black Sunglasses',
        3: 'Red Sunglasses',
        4: 'Yellow Sunglasses',
        5: 'Blue Sunglasses',
        6: 'Pink Sunglasses',
        7: 'Cyan Sunglasses',
        8: 'Green Sunglasses',
        9: 'Purple Sunglasses',
        10: 'Dark Red Sunglasses',
        11: 'Red Tinted Glasses',
        12: 'Grey Tinted Glasses',
        13: 'Lime Green Tinted Glasses',
        14: 'Light Purple Tinted Glasses',
        15: 'Orange Tinted Glasses',
        16: 'Mint Tinted Glasses',
        17: 'Dark Grey Tinted Glasses',
        18: 'Yellow Tinted Glasses',
        19: 'Regular Tinted Glasses',
        20: 'Bright Green Tinted Glasses'
    }
    return glassesDict