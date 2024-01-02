import pandas as pd
import os
import shutil
import socket
from transfers.training.predict import Predict

predictions = Predict()

def transfer_files(df: pd.DataFrame):
    if not df.empty:

        if check_for_duplicates(df):
            return

        for i in range(len(df)):
            source_dir = df.iloc[i, 0]
            dest_dir = df.iloc[i, 1]
            status = df.iloc[i, 2]

            if status != "pending":
                i += 1 if len(df) > i else 0
                continue

            os.makedirs(dest_dir, exist_ok=True)

            # Check if source is a directory
            if os.path.isdir(source_dir):
                # Copy the entire directory to the destination
                shutil.copytree(source_dir, dest_dir)
                print(f"Copied directory {source_dir} to {dest_dir}")
            else:
                # Get a list of all files in the source directory
                files = os.listdir(source_dir)

                # Move each file to the destination directory
                for file in files:
                    source_file = os.path.join(source_dir, file)
                    dest_file = os.path.join(dest_dir, file)
                    shutil.move(source_file, dest_file)
                    print(f"Moved {source_file} to {dest_file}")

            df.iloc[i, 2] = "completed"
            print(df.head())
            predictions.add_dataframe(df, "file")

    else:
        print("No files to transfer")

def transfer_files_over_network(df: pd.DataFrame):
    if not df.empty:

        if check_for_duplicates(df):
            return

        for i in range(len(df)):
            source_file = df.iloc[i, 0]
            dest_ip = df.iloc[i, 1]
            dest_port = df.iloc[i, 2]
            status = df.iloc[i, 3]

            if status != "pending":
                i += 1 if len(df) > i else 0
                continue

            # Create a socket object
            s = socket.socket()

            # Connect to the server
            s.connect((dest_ip, dest_port))

            # Open the file in binary mode
            with open(source_file, 'rb') as f:
                # Send file
                while True:
                    data = f.read(1024)
                    while (data):
                        s.send(data)
                        data = f.read(1024)

                    # Close the connection
                    s.close()

                    df.iloc[i, 3] = "completed"
                    print(df.head())
                    predictions.add_dataframe(df, "network")

    else:
        print("No files to transfer")

def check_for_duplicates(df: pd.DataFrame) -> bool:
    df_list = [source_dir for source_dir in df.iloc[:, 0]]

    # Check for duplicates
    if len(df_list) != len(set(df_list)):
        print("There are duplicates in the source directory list")

        return True
    else:
        return False

"""
Example data:

data = {
    "folder_path": ["C:/Users/alexa/OneDrive/Desktop/Python/Projects/", "C:/Users/alexa/OneDrive/Desktop"],
    "dest_folder_path": ["C:/Users/alexa/OneDrive/Desktop/Python/Projects/", "C:/Users/alexa/OneDrive/Desktop/Python/Projects/"],
    "status": ["pending", "pending"],
}

server_data = {
    "source_file": ["C:/path/to/source1"],
    "dest_ip": ["192.168.1.3"],
    "dest_port": [5000],
    "status": ["pending"]
}

"""