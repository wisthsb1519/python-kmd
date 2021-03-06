from os import environ
from os.path import expanduser
home = expanduser("~")

# change these after starting the node and kmd
# algod info is in the algod.net and algod.token files in the data directory
# kmd info is in the kmd.net and kmd.token files in the kmd directory in data
# change these after starting the node and kmd

# kmd_token = "e4a0aa0518da921bae3f27f40f443a4e154a1c80f25f7759db7767e04d73c06c"
# kmd_address = "http://localhost:7833"

# algod_token = "a967f42b017cd4c5c95a633e87b5ff14226ae60609e174bf5832722631946e13"
# algod_address = "http://localhost:8080"

# path to the data directory
data_dir_path = environ.get("ALGORAND_DATA", home + "/node/testnetdata")
kmd_folder_name = "kmd-v0.5"  # name of the kmd folder in the data directory

# get tokens and addresses automatically, if data_dir_path is not empty
if data_dir_path and kmd_folder_name:
    if not data_dir_path[-1] == "/":
        data_dir_path += "/"
    if not kmd_folder_name[-1] == "/":
        kmd_folder_name += "/"
    algod_token = open(data_dir_path + "algod.token", "r").read().strip("\n")
    algod_address = "http://" + open(data_dir_path + "algod.net",
                                     "r").read().strip("\n")
    kmd_token = open(data_dir_path + kmd_folder_name + "kmd.token",
                     "r").read().strip("\n")
    kmd_address = "http://" + open(data_dir_path + kmd_folder_name + "kmd.net",
                                   "r").read().strip("\n")
