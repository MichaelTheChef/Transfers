import pandas as pd
import os
import shutil

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

            # Get a list of all files in the source directory
            files = os.listdir(source_dir)

            # Move each file to the destination directory
            for file in files:
                source_file = os.path.join(source_dir, file)
                dest_file = os.path.join(dest_dir, file)
                shutil.move(source_file, dest_file)
                print(f"Moved {source_file} to {dest_file}")

            df.iloc[i, 2] = "completed"

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
}

"""

data = {
    "folder_path": ["C:/Users/alexa/OneDrive/Desktop/Python/Projects/", "C:/Users/alexa/OneDrive/Desktop/Python/Projecs/"],
    "dest_folder_path": ["C:/Users/alexa/OneDrive/Desktop/Python/Projects/", "C:/Users/alexa/OneDrive/Desktop/Python/Projects/"],
    "status": ["pending", "pending"],
}
df = pd.DataFrame(data)
e = [source_dir for source_dir in df.iloc[:, 0]]
print(e)
#transfer_files(df)