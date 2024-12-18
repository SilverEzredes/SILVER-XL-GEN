import os

# Set output file path and name
outputFilePath = "G:\\Cyberpunk 2077\\archive\\pc\\mod\\"
outputFileName = "YourCoolXLFile"

# Define ent file list
entList = [ 
    #FemV and FemNPC ents:
    "base\\characters\\entities\\player\\photo_mode\\player_wa_photomode.ent",
    "ep1\\characters\\entities\\player\\photo_mode\\player_wa_photomode_ep1.ent",
    "base\\characters\\entities\\player\\photo_mode\\alt_cunningham\\alt_photomode.ent",
    "base\\characters\\entities\\player\\photo_mode\\blue_moon\\bmuc_photomode.ent",
    "base\\characters\\entities\\player\\photo_mode\\evelyn_parker\\evelyn_photomode.ent",
    "base\\characters\\entities\\player\\photo_mode\\hanako_arasaka\\hanako_photomode.ent",
    "base\\characters\\entities\\player\\photo_mode\\judy_alvarez\\judy_photomode.ent",
    "base\\characters\\entities\\player\\photo_mode\\lizzy_wizzy\\lizzy_photomode.ent",
    "base\\characters\\entities\\player\\photo_mode\\meredith_stout\\meredith_photomode.ent",
    "ep1\\characters\\entities\\player\\photo_mode\\myers\\myers_photomode.ent",
    "base\\characters\\entities\\player\\photo_mode\\rogue_amendiares\\old_rogue_photomode.ent",
    "base\\characters\\entities\\player\\photo_mode\\panam_palmer\\panam_photomode.ent",
    "base\\characters\\entities\\player\\photo_mode\\purple_force\\pfuc_photomode.ent",
    "base\\characters\\entities\\player\\photo_mode\\red_menace\\rmuc_photomode.ent",
    "base\\characters\\entities\\player\\photo_mode\\rogue_amendiares\\young_rogue_photomode.ent",
    "ep1\\characters\\entities\\player\\photo_mode\\songbird\\songbird_photomode.ent",
]
# Define anims to append
animList = [ 
    "base\\animations\\ui\\photomode\\pmu\\photomode__female__idle_zwei_alt.anims",
]

print(f"\nSILVER-XL-GEN |==============================================================|")
if not os.path.exists(outputFilePath):
    print(f"\033[91mPath '{outputFilePath}' not found. Saving XL file next to the Python script.\033[0m")
    outputFilePath = os.path.dirname(os.path.abspath(__file__)) + os.sep

outputLines = []
outputLines.append("animations:")
for ent in entList:
    for anim in animList:
        outputLines.append(f" - entity: {ent}")
        outputLines.append(f"   set: {anim}")

outputFile = os.path.join(outputFilePath, outputFileName + ".archive.xl")
with open(outputFile, "w") as file:
    file.write("\n".join(outputLines))

print(f"\033[92mXL File saved to: {outputFile}\033[0m\n")