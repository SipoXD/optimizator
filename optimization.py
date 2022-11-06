import os, ctypes, shutil

windows_user = os.getenv("username")

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

if isAdmin() == False:
    exit()

try:
    os.system("sc stop sysmain & sc config sysmain start=disabled")
    os.system("sc stop diagtrack & sc config diagtrack start=disabled")  
    shutil.rmtree(r"C:\\Users\\" + windows_user + r"\\AppData\\Local\\Temp", ignore_errors=True)
    shutil.rmtree(r"C:\Windows\\Prefetch", ignore_errors=True)
    os.system("cls")
    print("Succesfully stopped diagtrack")
    print("Succesfully stopped sysmain")
    print("Succesfully deleted prefetch")
    print("Succesfully deleted %temp%")
    input("Press enter to exit...")
except:
    os.system("cls")
    input("Failed, press enter to exit...")
