from color_utils import SimpleColorMap, ColorDuplicatePicker, ColorMapWithShades
from texture_utils import GetTextureBits

armorPiecesList = ["head_front", "head_back", "torso_front", "torso_back", "leftArm_back", "leftArm_front", "leftHand_back", "leftHand_front", "rightArm_front", "vrightArm_back", "rightHand_front", "rightHand_back", "leftLeg_back", "leftLeg_front", "rightLeg_back", "rightLeg_front", "leftFoo_front", "leftFoot_back", "rightFoot_front", "rightFoot_back"]
amorPiecesVerticalList = ["head_front", "leftArm_back", "rightArm_front", "leftLeg_back", "rightFoot_front", "head_back", "leftArm_front", "rightArm_back", "leftLeg_front", "leftFoot_back", "torso_front", "leftHand_back", "rightHand_front", "rightLeg_back", "rightFoot_front", "torso_back", "leftHand_front", "rightHand_back", "rightLeg_front", "rightFoot_back"]
def main(): 
    # These are my presets for the map coloring. use the same parameters as your {obj}.map.png .
    # If you don't have a map, you can even color the silhouette with one color. this Funcion will cover the rest.

    # This is my PRESET
    # ColorTextureWithShades("./TestImages/Player.map.png", 64, 80, 16, "./TestImages/Player_reworked.map.png")

    GetTextureBits("./TestImages/Player_reworked.map.png", amorPiecesVerticalList, 16, 16, "./TestImages/BasicArmor/Player_basicArmor_", 4, 5)

if __name__ == "__main__":
    main()