import os
import shutil
uselessElements = ['inputoverlay-background.png','fail-background.png','fail-background@2x.png','pause-back.png','comboburst-0.png', 'comboburst-1.png', 'comboburst-2.png','comboburst-3.png', 'comboburst-4.png','comboburst-5.png', 'comboburst-6.png', 'comboburst-7.png', 'comboburst-8.png', 'comboburst-9.png','section-pass.png','section-fail.png','ranking-X.png','mod-autopilot.png', 'mod-cinema.png','hit100k.png','selection-mod-autoplay.png','selection-mod-autoplay@2x.png','selection-mod-cinema.png','selection-mod-cinema@2x.png','selection-mod-doubletime.png','selection-mod-doubletime@2x.png','selection-mod-easy.png','selection-mod-easy@2x.png','selection-mod-flashlight.png','selection-mod-flashlight@2x.png','selection-mod-halftime.png','selection-mod-halftime@2x.png','selection-mod-hardrock.png','selection-mod-hardrock@2x.png','selection-mod-hidden.png','selection-mod-hidden@2x.png','selection-mod-nightcore.png','selection-mod-nightcore@2x.png','selection-mod-nofail.png','selection-mod-nofail@2x.png','selection-mod-perfect.png','selection-mod-perfect@2x.png','selection-mod-relax.png','selection-mod-relax2.png','selection-mod-relax2@2x.png','selection-mod-relax@2x.png','selection-mod-scorev2.png','selection-mod-scorev2@2x.png','selection-mod-spunout.png','selection-mod-spunout@2x.png','selection-mod-suddendeath.png','selection-mod-suddendeath@2x.png','selection-mod-target.png','selection-mod-target@2x.png','selection-mode-over.png','selection-mode-over@2x.png','selection-mode.png','selection-mode@2x.png','selection-mods-over.png','selection-mods-over@2x.png','selection-mods.png','selection-options-over.png','selection-options-over@2x.png','selection-options.png','selection-random-over.png','selection-random-over@2x.png','selection-random.png','selection-tab.png','selection-tab@2x.png','button-right@2x.png','button-right.png','button-middle@2x.png','button-middle.png','button-left@2x.png','button-left.png', 'pause-back.png','pause-back@2x.png','pause-continue.png','pause-continue@2x.png','pause-overlay.png','pause-overlay@2x.png','pause-replay.png','pause-replay@2x.png','pause-retry.png','pause-retry@2x.png','pause-back.png','pause-back@2x.png','ranking-A-small.png','ranking-A-small@2x.png','ranking-A.png','ranking-A@2x.png','ranking-accuracy.png','ranking-B-small.png','ranking-B-small@2x.png','ranking-B.png','ranking-B@2x.png','ranking-C-small.png','ranking-C-small@2x.png','ranking-C.png','ranking-C@2x.png','ranking-D-small.png','ranking-D-small@2x.png','ranking-D.png','ranking-D@2x.png','ranking-graph.png','ranking-maxcombo.png','ranking-panel.png','ranking-panel@2x.png','ranking-perfect.png','ranking-perfect@2x.png','ranking-retry.png','ranking-retry@2x.png','ranking-S-small.png','ranking-S-small@2x.png','ranking-S.png','ranking-S@2x.png','ranking-SH-small.png','ranking-SH-small@2x.png','ranking-SH.png','ranking-SH@2x.png','ranking-title.png','ranking-title@2x.png','ranking-winner.png','ranking-winner@2x.png','ranking-X-small.png','ranking-X-small@2x.png','ranking-X.png','ranking-X@2x.png','ranking-XH-small.png','ranking-XH-small@2x.png','ranking-XH.png','ranking-XH@2x.png','arrow-pause.png','arrow-pause@2x.png','arrow-warning.png','arrow-warning@2x.png','menu-snow.png','menu-back-click.ogg','menu-back-hover.ogg','menu-back.png','menu-back@2x.png','menu-background.jpg','menu-button-background.png','menu-button-background@2x.png','menu-snow.png','section-fail@2x.png','section-pass@2x.png','sectionfail.ogg','sectionpass.ogg','selection-mod-fadein.png','selection-mod-fadein@2x.png','selection-mod-key1.png','selection-mod-key1@2x.png','selection-mod-key2.png','selection-mod-key2@2x.png','selection-mod-key3.png','selection-mod-key3@2x.png','selection-mod-key4.png','selection-mod-key4@2x.png','selection-mod-key5.png','selection-mod-key5@2x.png','selection-mod-key6.png','selection-mod-key6@2x.png','selection-mod-key7.png','selection-mod-key7@2x.png','selection-mod-key8.png','selection-mod-key8@2x.png','selection-mod-key9.png','selection-mod-key9@2x.png','selection-mod-keycoop.png','selection-mod-keycoop@2x.png','selection-mod-mirror.png','selection-mod-mirror@2x.png','selection-mod-random.png','selection-mod-random@2x.png','selection-mods@2x.png','selection-options@2x.png','selection-random@2x.png','mode--small.png','mode--small@2x.png','mode-fruits-small.png','mode-fruits-small@2x.png','mode-fruits.png','mode-mania-small.png','mode-mania-small@2x.png','mode-mania.png','mode-osu-med.png','mode-osu-med@2x.png','mode-osu-small.png','mode-osu-small@2x.png','mode-osu.png','mode-taiko-small.png','mode-taiko-small@2x.png','mode-taiko.png','mode-taiko@2x.png', 'welcome_text.png''welcome_text@2x.png','count.wav','count1.png','count1@2x.png','count1s.ogg','count1s.wav','count2.png','count2@2x.png','count2s.ogg','count2s.wav','count3.png','count3@2x.png','count3s.ogg','count3s.wav', 'ready.png','ready@2x.png','readys.wav','ranking-A - Copy.png','ranking-A-small - Copy.png','ranking-A-small@2x - Copy.png','ranking-B - Copy.png','ranking-B-small - Copy.png','ranking-B-small@2x - Copy.png','ranking-C - Copy.png','ranking-C-small - Copy.png','ranking-C-small@2x - Copy.png','ranking-D - Copy.png','ranking-D-small - Copy.png','ranking-D-small@2x - Copy.png','ranking-graph@2x.png','ranking-panel-bottom.png','ranking-panel-bottom@2x.png','ranking-panel@2xold.png','ranking-replay.png','ranking-replay@2x.png','ranking-X - Copy.png','ranking-XH - Copy.png','scoreentry-0.png','scoreentry-0@2x.png','scoreentry-1.png','scoreentry-1@2x.png','scoreentry-2.png','scoreentry-2@2x.png','scoreentry-3.png','scoreentry-3@2x.png','scoreentry-4.png','scoreentry-4@2x.png','scoreentry-5.png','scoreentry-5@2x.png','scoreentry-6.png','scoreentry-6@2x.png','scoreentry-7.png','scoreentry-7@2x.png','scoreentry-8.png','scoreentry-8@2x.png','scoreentry-9.png','scoreentry-9@2x.png','scoreentry-comma.png','scoreentry-comma@2x.png','scoreentry-x.png','scoreentry-x@2x.png',
]
count = 0
print("Made by Brinex.\nWith love <3!")
# Creates the "debloated.txt" file in the debloated skin folder
def settingsFileCreation(settingsFile):
    if not os.path.exists(settingsFile):
        with open(settingsFile, "w"):
            print(f"File '{settingsFile}' Created \n")

# Sets the default skin path
def defaultSkinFolder():
    global count,skinDir
    # First setup 
    if count == 0:
        skinDir = input(r"Path to skin directory (usually in C:\Users\YourName\Appdata\Roaming\osu!\Skins): ")
        count+=1
    # Triggers when changing the skin folder path
    else:
        skinDir = input(r"Path to skin directory (usually in C:\Users\YourName\Appdata\Roaming\osu!\Skins): ")
        copyFiles()


# The main menu
def mainMenu():
    print("\n\n\n1.Debloat skin\n"+"2.Only Delete x2 (If you use high resolutions, don't do this!)\n"+"3.Debloat animations"+"\n4.Change skin folder path\n5.Exit")
    p = input()
    if p == "5":
        exit()
    elif p == "1":
        debloat()
    elif p == "2":
        debloat2x()
    elif p == "3":
        debloatAnimation()
    elif p == "4":
        defaultSkinFolder()
    else:
        print("Invalid option\n")
    while p != "5":
        return mainMenu()


# Copies everything from the skin folder to the Debloated {Skin Name}
def copyFiles():
    global skinDir,copied_skin_dir,settingsFile
    original_skin_dir = skinDir
    copied_skin_dir = os.path.join(os.path.dirname(skinDir),"Debloated "+ os.path.basename(skinDir).strip())
    settingsFile = copied_skin_dir +"\debloated.txt"
    def copyFunction():
        try:
            shutil.copytree(original_skin_dir, copied_skin_dir)
            settingsFileCreation(settingsFile)
            print(f"Folder '{original_skin_dir}' copied to '{copied_skin_dir}'")
            skinDir = copied_skin_dir
            print(f"Successfully created a debloated skin folder at '{copied_skin_dir}'")
            mainMenu()
        except shutil.Error as e:
            print(f"Error: {e}")
    
    if os.path.exists(copied_skin_dir):
        d = input("Do you want to remove the previously debloated folder? Y/n\n")
        if d.lower == "y":
            shutil.rmtree(copied_skin_dir)
            print("\nRemoved Old Debloated Folder")
            copyFunction()
        else:
            print("Skipped previous file removal")
            mainMenu()
    else:
        copyFunction()


# Deletes every 2x@ file
def debloat2x():
    global skinDir,settingsFile
    os.chdir(skinDir)
    found = False
    if os.path.exists(settingsFile):
        with open(settingsFile, "r+") as file:
            lines = file.readlines()
    
            for line in lines:
                if "Debloated2X" in line:
                    found = True
                    break
                
            if not found:
                file.seek(0,2)
                file.write("Debloated2X\n")
                
    
        if found == False:
            print("REMOVING 2X")
            files_in_directory = os.listdir(skinDir)
            filtered_array = [item for item in files_in_directory if '2x' in item]
            for file_name in filtered_array:
                if os.path.exists(file_name):
                    os.remove(file_name)
                    print(f"File '{file_name}' has been successfully deleted.")
    
        else:
            print("\n\nAlready Used 2X Debloating")
    else:
        settingsFileCreation(settingsFile)
        return debloat2x()

# Deletes selected number of frames
def debloatAnimation():
    print("DEBLOATING ANIMATIONS")
    files_in_directory = os.listdir(skinDir)
    count1 = 0
    found = False
    if os.path.exists(settingsFile):
        with open(settingsFile, "r+") as file:
            lines = file.readlines()
            file.seek(0,2)
            for line in lines:
                if "AnimationDebloating" in line:
                    found = True
                    break

            if not found:
                file.seek(0,2)
                file.write("AnimationDebloating\n")

        if found == False:    
            h = input("How many frames apart do you want to delete? (larger number means less frames deleted) (1-4)")
            while h not in ["1", "2", "3", "4"]:
                h = input("Invalid input. Please enter a number between 1 and 4: ")
            h = int(h)
            if h > 4:
                h = 4

            for file_name in files_in_directory:
                if file_name.startswith(("hit0-","hit50-","hit100-","hit100k-")) and file_name.endswith(".png"):
                    count1 += 1
                    if count1 % h == 0:
                        file_path = os.path.join(skinDir, file_name)
                        os.remove(file_path)
                        print(f"Deleted: {file_name}")
        else:
            print("\n\nAlready Used Animation Debloating")
    else:
        settingsFileCreation(settingsFile)
        return debloatAnimation()

# Deletes unnecessary skin files
def debloat():
    found = False
    if os.path.exists(settingsFile):
        with open(settingsFile, "r+") as file:
            lines = file.readlines()
            for line in lines:
                if "Debloated" in line:
                    found = True
                    break

            if not found:
                file.seek(0,2)
                file.write("Debloated\n")
    else:
        settingsFileCreation(settingsFile)
        return debloat()
    if found == False: 
        print("DEBLOATING SKIN")
        os.chdir(skinDir)
        for file_name in uselessElements:
            if os.path.exists(file_name):
                os.remove(file_name)
                print(f"File '{file_name}' has been successfully deleted.")
    else:
        print("\n\nAlready Used Skin Debloating")  

# Calls the Default folder selecting function
defaultSkinFolder()

# Copy folder function
copyFiles()

