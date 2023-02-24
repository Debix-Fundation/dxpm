import sys
import os
import platform

version = 1.0

if platform.system() != "Linux":
    print("DebiX Package Manager only works on Linux")
    sys.exit(1)

def download_package(package):
    os.system("wget " + package)

def install_package(package):
    os.system("wget " + package)
    os.system("dpkg -i " + package)

def remove_package(package):
    os.system("dpkg -r " + package)

def show_help():
    print("DebiX Package Manager")
    print("Version "+ str(version))
    print("Usage: dxpm [action] [package]")
    print("Actions:")
    print("install: Install package")
    print("remove: Remove package")
    print("help: Show this help")

if len(sys.argv) < 3:
    show_help()
    sys.exit(1)

action = sys.argv[1]
package = sys.argv[2]


if action == "install":
    install_package(package)
elif action == "remove":
    remove_package(package)
elif action == "download":
    download_package(package)
elif action == "help":
    show_help()
else:
    print("Invalid action")
    show_help()
    sys.exit(1)
