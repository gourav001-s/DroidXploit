import os
import sys

# ==================================================
# Terminal Colors
# ==================================================
class C:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

# ==================================================
# Helpers
# ==================================================
def pause():
    input(C.YELLOW + "\nPress ENTER to continue..." + C.RESET)

def banner():
    os.system("clear")
    print(C.CYAN + C.BOLD + "=" * 70 + C.RESET)
    print(C.CYAN + C.BOLD + r"""
 █████╗ ███╗   ██╗██████╗ ██████╗  ██████╗ ██╗██████╗ 
██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██║██╔══██╗
███████║██╔██╗ ██║██║  ██║██████╔╝██║   ██║██║██║  ██║
██╔══██║██║╚██╗██║██║  ██║██╔══██╗██║   ██║██║██║  ██║
██║  ██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║██████╔╝
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ 
""" + C.RESET)
    print(C.GREEN + C.BOLD + "        AndroidXploit Framework" + C.RESET)
    print(C.YELLOW + "        Developed by: " + C.BOLD + "RaVX" + C.RESET)
    print(C.BLUE + "        Rooted Emulator | ADB | Frida | Python" + C.RESET)
    print(C.CYAN + C.BOLD + "=" * 70 + C.RESET)

# ==================================================
# Core Modules
# ==================================================
def enum_device():
    print(C.GREEN + "\n[+] Device Enumeration\n" + C.RESET)
    cmds = [
        "adb devices",
        "adb shell id",
        "adb shell getprop ro.build.version.release",
        "adb shell getprop ro.build.version.sdk",
        "adb shell uname -a"
    ]
    for c in cmds:
        os.system(c)
    pause()

def enum_apps():
    print(C.GREEN + "\n[+] Installed Applications\n" + C.RESET)
    os.system("adb shell pm list packages")
    pause()

def dump_app_data():
    pkg = input("Package name: ").strip()
    print(C.GREEN + "\n[+] Dumping App Data\n" + C.RESET)
    os.system(f"adb pull /data/data/{pkg} dump_{pkg}")
    pause()

def token_hunter():
    pkg = input("Package name: ").strip()
    print(C.GREEN + "\n[+] Token Hunting\n" + C.RESET)
    os.system(
        f'adb shell su -c "grep -R \'token\\|jwt\\|apikey\' /data/data/{pkg} 2>/dev/null"'
    )
    pause()

def ssl_pinning():
    pkg = input("Package name: ").strip()
    script = input("Frida script path: ").strip()
    print(C.GREEN + "\n[+] Launching Frida\n" + C.RESET)
    os.system(f"frida -U -f {pkg} -l {script} --no-pause")
    pause()

def memory_inspect():
    pkg = input("Package name: ").strip()
    print(C.GREEN + "\n[+] Memory Inspection\n" + C.RESET)
    os.system(f"adb shell pidof {pkg}")
    pause()

def system_logs():
    print(C.YELLOW + "\n[!] Press CTRL+C to stop logcat\n" + C.RESET)
    os.system("adb logcat")
    pause()

def bypass_checks():
    print(C.GREEN + "\n[+] Root / Emulator Checks\n" + C.RESET)
    os.system("adb shell getprop ro.kernel.qemu")
    os.system("adb shell which su")
    pause()

def persistence():
    print(C.RED + "\n[!] Emulator Persistence (Use Carefully)\n" + C.RESET)
    os.system("adb shell su -c 'touch /system/bin/persist_test'")
    pause()

# ==================================================
# Advanced Modules
# ==================================================
def preflight_check():
    print(C.GREEN + "\n[+] Pre-Flight Environment Check\n" + C.RESET)
    checks = [
        "adb version",
        "adb devices",
        "adb shell su -c id",
        "frida --version",
        "python3 --version"
    ]
    for c in checks:
        os.system(c)
    pause()

def app_intel():
    pkg = input("Package name: ").strip()
    print(C.GREEN + "\n[+] App Intelligence\n" + C.RESET)
    os.system(f"adb shell dumpsys package {pkg} | grep version")
    os.system(f"adb shell dumpsys package {pkg} | grep debuggable")
    os.system(f"adb shell dumpsys package {pkg} | grep backup")
    pause()

def advanced_secret_hunter():
    pkg = input("Package name: ").strip()
    print(C.GREEN + "\n[+] Advanced Secret Hunting\n" + C.RESET)
    patterns = "token|jwt|apikey|https?://|password|email"
    os.system(
        f'adb shell su -c "grep -R \'{patterns}\' /data/data/{pkg} 2>/dev/null"'
    )
    pause()

def sqlite_intel():
    pkg = input("Package name: ").strip()
    print(C.GREEN + "\n[+] SQLite Intelligence\n" + C.RESET)
    os.system(f"adb shell su -c 'ls /data/data/{pkg}/databases'")
    pause()

def frida_manager():
    pkg = input("Package name: ").strip()
    print(C.GREEN + "\n[+] Frida Interactive Session\n" + C.RESET)
    os.system(f"frida -U -f {pkg}")
    pause()

def runtime_assist():
    pkg = input("Package name: ").strip()
    print(C.GREEN + "\n[+] Runtime Assistant\n" + C.RESET)
    os.system(f"adb shell pidof {pkg}")
    os.system(f"adb shell su -c 'cat /proc/$(pidof {pkg})/maps | grep ssl'")
    pause()

def full_assessment():
    print(C.CYAN + "\n[+] Full App Assessment Started\n" + C.RESET)
    app_intel()
    dump_app_data()
    advanced_secret_hunter()
    sqlite_intel()
    print(C.GREEN + "\n[+] Assessment Completed\n" + C.RESET)
    pause()

def generate_report():
    with open("androidxploit_report.md", "w") as f:
        f.write("# AndroidXploit Security Assessment\n")
        f.write("Developed by RaVX\n")
    print(C.GREEN + "[+] Report generated: androidxploit_report.md" + C.RESET)
    pause()

# ==================================================
# Command Registry (Framework Core)
# ==================================================
COMMANDS = {
    "1": ("Device Enumeration", enum_device),
    "2": ("Installed Apps", enum_apps),
    "3": ("Dump App Data", dump_app_data),
    "4": ("Token Hunter", token_hunter),
    "5": ("SSL Pinning (Frida)", ssl_pinning),
    "6": ("Memory Inspection", memory_inspect),
    "7": ("System Logs", system_logs),
    "8": ("Root / Emulator Checks", bypass_checks),
    "9": ("Persistence (Emulator)", persistence),
    "10": ("Pre-Flight Check", preflight_check),
    "11": ("App Intelligence", app_intel),
    "12": ("Advanced Secret Hunter", advanced_secret_hunter),
    "13": ("SQLite Intelligence", sqlite_intel),
    "14": ("Frida Manager", frida_manager),
    "15": ("Runtime Assistant", runtime_assist),
    "16": ("Full App Assessment", full_assessment),
    "17": ("Report Generator", generate_report),
    "0": ("Exit", None)
}

# ==================================================
# Menu & Main Loop
# ==================================================
def menu():
    print("\n" + C.WHITE + C.BOLD + "Available Modules:" + C.RESET)
    for k in sorted(COMMANDS, key=lambda x: int(x) if x.isdigit() else 999):
        print(C.CYAN + f"[{k}]" + C.RESET + " " + C.GREEN + COMMANDS[k][0] + C.RESET)

def main():
    banner()
    while True:
        menu()
        choice = input(C.YELLOW + "\nSelect option: " + C.RESET).strip()

        if choice == "0":
            print(C.RED + "Exiting..." + C.RESET)
            sys.exit(0)

        command = COMMANDS.get(choice)
        if command:
            command[1]()
        else:
            print(C.RED + "[!] Invalid option" + C.RESET)

# ==================================================
if __name__ == "__main__":
    main()
