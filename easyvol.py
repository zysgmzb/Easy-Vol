# coding: utf-8
import subprocess
import os

banner = """

▓█████ ▄▄▄        ██████▓██   ██▓    ██▒   █▓ ▒█████   ██▓    
▓█   ▀▒████▄    ▒██    ▒ ▒██  ██▒   ▓██░   █▒▒██▒  ██▒▓██▒    
▒███  ▒██  ▀█▄  ░ ▓██▄    ▒██ ██░    ▓██  █▒░▒██░  ██▒▒██░    
▒▓█  ▄░██▄▄▄▄██   ▒   ██▒ ░ ▐██▓░     ▒██ █░░▒██   ██░▒██░    
░▒████▒▓█   ▓██▒▒██████▒▒ ░ ██▒▓░      ▒▀█░  ░ ████▓▒░░██████▒
░░ ▒░ ░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ██▒▒▒       ░ ▐░  ░ ▒░▒░▒░ ░ ▒░▓  ░
 ░ ░  ░ ▒   ▒▒ ░░ ░▒  ░ ░▓██ ░▒░       ░ ░░    ░ ▒ ▒░ ░ ░ ▒  ░
   ░    ░   ▒   ░  ░  ░  ▒ ▒ ░░          ░░  ░ ░ ░ ▒    ░ ░   
   ░  ░     ░  ░      ░  ░ ░              ░      ░ ░      ░  ░
                         ░ ░             ░                    


author: zysgmzb
"""


def get_online_profile():
    return


class Windows:
    def __init__(self, filepath):
        self.filepath = filepath
        self.profile = ''

    def winmenu(self):
        os.system('clear')
        banner = """
 _       ___           __                  
| |     / (_)___  ____/ /___ _      _______
| | /| / / / __ \/ __  / __ \ | /| / / ___/
| |/ |/ / / / / / /_/ / /_/ / |/ |/ (__  ) 
|__/|__/_/_/ /_/\__,_/\____/|__/|__/____/ 


        """
        print(banner)
        if (self.profile == ''):
            print("1. Show profiles list")
            print("2. Select profile manually")
            print("3. Auto select profile")
            print("0. Exit")
            chos = input("Please enter your choice > ").strip()
            if (chos == '1'):
                self.get_profile_list()
                input("Press enter to continue ...")
                self.winmenu()
            elif (chos == '2'):
                self.select_profile()
                input("Press enter to continue ...")
                self.winmenu()
            elif (chos == '3'):
                self.analysis_image()
                input("Press enter to continue ...")
                self.winmenu()
            elif (chos == '0'):
                print("Bye ~")
                exit()
            else:
                print("Invalid input")
                input("Press enter to continue ...")
                self.winmenu()
        else:
            print("1. Show pslist")
            print("2. scan the file")
            print("3. Display basic information")
            print("4. Display more information")
            print("5. Dump the process memory")
            print("6. Dump the file")
            print("7. Back to the profile selection page")
            print("0. Exit")
            chos = input("Please enter your choice > ").strip()
            if (chos == '1'):
                self.analysis_ps()
                input("Press enter to continue ...")
                self.winmenu()
            elif (chos == '2'):
                self.analysis_file()
                input("Press enter to continue ...")
                self.winmenu()
            elif (chos == '3'):
                self.analysis_common_records()
                input("Press enter to continue ...")
                self.winmenu()
            elif (chos == '4'):
                self.more_records()
                input("Press enter to continue ...")
                self.winmenu()
            elif (chos == '5'):
                self.dump_ps_mem()
                input("Press enter to continue ...")
                self.winmenu()
            elif (chos == '6'):
                self.dump_file()
                input("Press enter to continue ...")
                self.winmenu()
            elif (chos == '7'):
                self.profile = ''
                self.winmenu()
            elif (chos == '0'):
                print("Bye ~")
                exit()
            else:
                print("Invalid input")
                input("Press enter to continue ...")
                self.winmenu()
        return 1

    def get_profile_list(self):
        cmd = "python2 ./volatility/vol.py --info | grep 'Profile for Windows'"
        print("Just Wait ...")
        print()
        prolistres = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().split('\n')
        prolistres = [i.split(' ')[0] for i in prolistres]
        print('\n'.join(prolistres))
        return prolistres

    def select_profile(self):
        print("The following are all currently existing profiles")
        allpro = self.get_profile_list()
        pro_chos = input("Please enter the profile you want to use : ").strip()
        if (pro_chos in allpro):
            print("Well, the selected profile is : ", pro_chos)
            self.profile = pro_chos
            return 1
        else:
            print("The profile you input does not exist")
            return 0

    def analysis_image(self):
        if (self.profile != ''):
            print("You have already selected a profile")
            chos = input("Continue? (Y/N) > ").lower()
            if (chos == 'y' or chos == 'yes'):
                print("Well")
                print()
            else:
                return 0
        cmd = f"python2 ./volatility/vol.py -f {self.filepath} imageinfo | grep 'Suggested Profile'"
        print("Just Wait (may take a long time)...")
        imageprores = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().strip()
        print(imageprores)
        print()
        cho = imageprores.split(' ')[3].strip(',')
        print(f"The selected profile is : {cho}")
        self.profile = cho
        return 1

    def analysis_ps(self):
        cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} pslist"
        print("Pslist is running ...")
        print("Just Wait ...")
        print()
        pslistres = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().strip()
        print(pslistres)
        print()
        return pslistres

    def analysis_file(self):
        cho = input(
            "Auto search for suspicious filename or custom (a/c) > ").lower().strip()
        if (cho == 'a' or cho == 'auto'):
            cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} filescan | grep -E '桌面\\\|Desktop\\\|Documents\\\|flag|hint|secret|.zip$|.txt$|.rar$|.7z$|.png$|.jpg$|.gif$|.pdf$|.doc$|.docx$|.pcap$|.pcapng$'"
            print("Just Wait ...")
            print()
            filescanres = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().strip()
            print(filescanres)
        elif (cho == 'c' or cho == 'custom'):
            chos = input(
                "Please enter the keyword you want to search > ").strip()
            cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} filescan | grep -E '{chos}' "
            print("Just Wait ...")
            print()
            filescanres = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().strip()
            print(filescanres)
        return filescanres

    def analysis_common_records(self):
        typelist = ['cmdscan', 'notepad', 'editbox', 'iehistory',
                    'psscan', 'mimikatz', 'envars']
        typelist2 = ['screenshot', 'clipboard']  # require parameters
        typelist3 = typelist+typelist2
        print("Here are some basic information : ")
        print()
        for i in typelist3:
            print(i)
        print()
        type = input(
            "Please enter the type of information you want to view > ").lower().strip()
        if (type not in typelist3):
            print(
                'The type you input does not exist here, go to "Display more information"')
            return 0
        if (type in typelist):
            cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} {type}"
            print("You have selected the following type : ", type)
            print("Just Wait ...")
            print()
            recordres = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().strip()
            print(recordres)
            print()
        else:
            if (type == 'screenshot'):
                cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} {type} -D ./screenshots"
                print("You have selected the following type : ", type)
                print("Just Wait ...")
                print()
                if (not os.path.exists('./screenshots')):
                    os.system('mkdir screenshots')
                recordres = subprocess.Popen(
                    cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().strip()
                print("The screenshot has been saved to ./screenshots")
            elif (type == 'clipboard'):
                cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} {type} -v"
                print("You have selected the following type : ", type)
                print("Just Wait ...")
                print()
                recordres = subprocess.Popen(
                    cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().strip()
                print(recordres)
                print()

        return 1

    def more_records(self):
        cho = input(
            'Please enter the type of record you want to view(such as "hivelist")> ').strip()
        cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} {cho}"
        print("Just Wait ...")
        print()
        morerecordres = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().strip()
        print(morerecordres)
        print()
        return

    def dump_ps_mem(self):
        allps = self.analysis_ps().split('\n')[2:]
        print()
        allpsname = [i[11:32].strip().split('.')[0] for i in allps]
        allpid = [i[32:38].strip() for i in allps]
        pid = input(
            "Please enter the pid of the process you want to dump > ").strip()
        if (pid not in allpid):
            print("The pid you input does not exist")
            return 0
        psname = allpsname[allpid.index(pid)]
        if (not os.path.exists('./psdumps')):
            os.system('mkdir psdumps')
        cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} memdump -p {pid} -D ./psdumps"
        print("Just Wait ...")
        print()
        dumpres = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE).stdout.read().decode().strip()
        os.rename(f"./psdumps/{pid}.dmp", f"./psdumps/{psname}.dmp")
        print("The memory dump has been saved to ./psdumps")
        print(f"name of this file : {psname}.dmp")
        return 1

    def all_file(self):
        cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} filescan"
        allfileres = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().strip()
        return allfileres

    def dump_file(self):
        addr = input(
            "Please enter the virtual address of the file you want to dump > ").strip()
        print("Just Wait ...")
        print()
        allfile = self.all_file().split('\n')[2:]
        allfileaddr = [i[0:18] for i in allfile]
        allfilename = [i.split('\\')[-1].strip() for i in allfile]
        if (addr not in allfileaddr):
            print("The virtual address you input does not exist")
            return 0
        if (not os.path.exists('./filedumps')):
            os.system('mkdir filedumps')
        filename = allfilename[allfileaddr.index(addr)]
        cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} dumpfiles -Q {addr} -D ./filedumps -n"
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE).stdout.read().decode().strip()
        file_in_dir = os.listdir('./filedumps')
        for i in file_in_dir:
            if (filename in i):
                os.rename(f"./filedumps/{i}", f"./filedumps/{filename}")
        print("The file dump has been saved to ./filedumps")
        print(f"name of this file : {filename}")
        return


class Linux:
    def __init__(self, filepath):
        self.filepath = filepath
        self.profile = ''

    def linuxmenu(self):
        os.system('clear')
        banner = """
    __    _                 
   / /   (_)___  __  ___  __
  / /   / / __ \/ / / / |/_/
 / /___/ / / / / /_/ />  <  
/_____/_/_/ /_/\__,_/_/|_|  
                            

        """
        print(banner)
        if (self.profile == ''):
            print("1. Show profiles list")
            print("2. Find linux version in image")
            print("3. Select profile manually")
            print("0. Exit")
            chos = input("Please enter your choice > ").strip()
            if (chos == '1'):
                self.get_profile_list()
                input("Press enter to continue ...")
                self.linuxmenu()
            elif (chos == '2'):
                self.analysis_linuxversion()
                input("Press enter to continue ...")
                self.linuxmenu()
            elif (chos == '3'):
                self.select_profile()
                input("Press enter to continue ...")
                self.linuxmenu()
            elif (chos == '0'):
                print("Bye ~")
                exit()
            else:
                print("Invalid input")
                input("Press enter to continue ...")
                self.linuxmenu()
        else:
            print("1. Show bash history")
            print("2. Show pslist")
            print("3. scan the file manually")
            print("4. Display more information")
            print("5. Dump the file")
            print("6. recover the whole file system (recommend)")
            print("7. Back to the profile selection page")
            print("0. Exit")
            chos = input("Please enter your choice > ").strip()
            if (chos == '1'):
                self.analysis_commands()
                input("Press enter to continue ...")
                self.linuxmenu()
            elif (chos == '2'):
                self.analysis_ps()
                input("Press enter to continue ...")
                self.linuxmenu()
            elif (chos == '3'):
                self.analysis_file()
                input("Press enter to continue ...")
                self.linuxmenu()
                self.linuxmenu()
            elif (chos == '4'):
                self.more_records()
                input("Press enter to continue ...")
                self.linuxmenu()
            elif (chos == '5'):
                self.dump_file()
                input("Press enter to continue ...")
                self.linuxmenu()
            elif (chos == '6'):
                self.recover_filesystem()
                input("Press enter to continue ...")
                self.linuxmenu()
            elif (chos == '7'):
                self.profile = ''
                self.linuxmenu()
            elif (chos == '0'):
                print("Bye ~")
                exit()
            else:
                print("Invalid input")
                input("Press enter to continue ...")
                self.linuxmenu()
        return 1

    def get_profile_list(self):
        cmd = "python2 ./volatility/vol.py --info | grep 'Profile for Linux'"
        print("Just Wait ...")
        print()
        prolistres = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().split('\n')
        prolistres = [i.split(' ')[0] for i in prolistres]
        print('\n'.join(prolistres))
        return prolistres

    def analysis_linuxversion(self):
        cmd = f"strings {self.filepath} | grep -E 'Linux version'"
        print("Just Wait ...")
        print()
        linuxversionres = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().strip()
        print(linuxversionres)
        print()
        return 1

    def select_profile(self):
        print("The following are all currently existing profiles")
        allpro = self.get_profile_list()
        pro_chos = input("Please enter the profile you want to use : ").strip()
        if (pro_chos in allpro):
            print("Well, the selected profile is : ", pro_chos)
            self.profile = pro_chos
            return 1
        else:
            print("The profile you input does not exist")
            return 0

    def analysis_commands(self):
        cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} linux_bash"
        print("Just Wait ...")
        print()
        bashres = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE).stdout.read().decode().strip()
        print(bashres)
        print()
        return 1

    def analysis_ps(self):
        cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} linux_pslist"
        print("Just Wait ...")
        print()
        pslistres = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().strip()
        print(pslistres)
        print()
        return 1

    def analysis_file(self):
        print("Auto search for suspicious filename is not supported for linux because it is too slow")
        print("I recommend you to recover the whole file system directly")
        cho = input("Still want to continue? (Y/N) > ").lower().strip()
        if (cho == 'y' or cho == 'yes'):
            print("Well")
            print()
            filename = input("Please enter the filename you want to search > ")
            cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} linux_enumerate_files | grep {filename}"
            print("Just Wait ...")
            print()
            filescanres = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().strip()
            print(filescanres)
            print()
        else:
            return 0
        return 1

    def more_records(self):
        cho = input(
            'Please enter the type of record you want to view(such as "linux_netstat")> ').strip()
        cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} {cho}"
        print("Just Wait ...")
        print()
        morerecordres = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().decode().strip()
        print(morerecordres)
        print()
        return 1

    def dump_file(self):
        addr = input(
            "Please enter the virtual address of the file you want to dump > ").strip()
        print("Just Wait ...")
        print()
        cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} linux_find_file -i {addr} -O ./filedumps/{addr}.dat"
        if (not os.path.exists('./filedumps')):
            os.system('mkdir filedumps')
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE).stdout.read().decode().strip()
        print("The file dump has been saved to ./filedumps")
        print(f"name of this file : {addr}.dat")
        print()
        return 1

    def recover_filesystem(self):
        print("Take a coffee and do something else")
        print("This will take a long time")
        cmd = f"python2 ./volatility/vol.py -f {self.filepath} --profile={self.profile} linux_recover_filesystem -D ./filesystem"
        if (not os.path.exists('./filesystem')):
            os.system('mkdir filesystem')
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE).stdout.read().decode().strip()
        print("The file system has been recovered to ./filesystem")
        print("done")
        print()
        return 1


def check_path():
    if (not os.path.exists('./volatility')):
        print("Please put volatility in the current directory")
        exit()


def main():
    print(banner)
    check_path()
    filepath = input("Please enter the path of the memory image > ").strip()
    OS = input(
        "Please enter the operating system of the memory image (Windows/Linux) > ").strip().lower()
    if (OS == 'windows' or OS == 'win' or OS == 'w'):
        winwinwin = Windows(filepath)
        winwinwin.winmenu()
    elif (OS == 'linux' or OS == 'lin' or OS == 'l'):
        linuxlinuxlinux = Linux(filepath)
        linuxlinuxlinux.linuxmenu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
