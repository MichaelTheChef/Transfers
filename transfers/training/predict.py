import pandas as pd

class Predict:
    def __init__(self):
        self.recent_file_df = None
        self.recent_network_df = None

        self.file_source_predictions = []
        self.file_dest_predictions = []
        self.network_source_predictions = []
        self.network_dest_predictions = []
        self.network_port_predictions = []


    def add_dataframe(self, df: pd.DataFrame, transfer_type: str) -> str:
        if not df.empty:
            if transfer_type == "file" and self.recent_file_df is not None:
                print("Predicting files...")

                source_directories = [df.iloc[i, 0] for i in range(len(df))]
                dest_directories = [df.iloc[i, 1] for i in range(len(df))]

                bool_sources = [(True, i) for i, item in enumerate(source_directories) if item in self.recent_file_df.iloc[:, 0]]
                bool_dests = [(True, i) for i, item in enumerate(dest_directories) if item in self.recent_file_df.iloc[:, 1]]

                if bool_sources:
                    for i in range(len(bool_sources)):
                        self.file_source_predictions.append(self.recent_file_df.iloc[(bool_sources[i][1]), 0])
                else:
                    print("No source predictions")

                if bool_dests:
                    for i in range(len(bool_dests)):
                        self.file_dest_predictions.append(self.recent_file_df.iloc[(bool_dests[i][1]), 1])
                else:
                    print("No destination predictions")


                return f"Sources Predictions: {bool_sources if bool_sources else None}, Destinations Predictions: {bool_dests if bool_dests else None}"

            elif transfer_type == "network" and self.recent_network_df is not None:
                print("Predicting network transfers...")

                source_files = [df.iloc[i, 0] for i in range(len(df))]
                dest_ip = [df.iloc[i, 1] for i in range(len(df))]
                dest_port = [df.iloc[i, 2] for i in range(len(df))]

                bool_sources = [(True, i) for i, item in enumerate(source_files) if item in self.recent_network_df.iloc[:, 0]]
                bool_dests = [(True, i) for i, item in enumerate(dest_ip) if item in self.recent_network_df.iloc[:, 1]]
                bool_ports = [(True, i) for i, item in enumerate(dest_port) if item in self.recent_network_df.iloc[:, 2]]

                if bool_sources:
                    for i in range(len(bool_sources)):
                        self.network_source_predictions.append(self.recent_network_df.iloc[(bool_sources[i][1]), 0])
                else:
                    print("No network source predictions")

                if bool_dests:
                    for i in range(len(bool_dests)):
                        self.network_dest_predictions.append(self.recent_network_df.iloc[(bool_dests[i][1]), 1])
                else:
                    print("No network destination predictions")

                if bool_ports:
                    for i in range(len(bool_ports)):
                        self.network_port_predictions.append(self.recent_network_df.iloc[[(bool_ports[i][1]), 2])
                else:
                    print("No network port predictions")


                return (f"Sources Predictions: {bool_sources if bool_sources else None}, "
                        f"Destinations Predictions: {bool_dests if bool_dests else None}, "
                        f"Ports Predictions: {bool_ports if bool_ports else None}")

            elif transfer_type == "file" and self.recent_file_df is None:
                print("No recent file transfers to predict, saved dataframe for future comparisons")
                self.update_recent_transfers(df, transfer_type)
                return "No recent file transfers to predict"

            elif transfer_type == "network" and self.recent_network_df is None:
                print("No recent network transfers to predict, saved dataframe for future comparisons")
                self.update_recent_transfers(df, transfer_type)
                return "No recent network transfers to predict"

        else:
            print("No files to predict")

    def get_predictions(self, transfer_type: str):
        if transfer_type == "file":
            return self.file_source_predictions, self.file_dest_predictions

        elif transfer_type == "network":
            return self.network_source_predictions, self.network_dest_predictions, self.network_port_predictions

    def update_recent_transfers(self, df: pd.DataFrame, transfer_type: str):
        if transfer_type == "file":
            self.recent_file_df = df
        elif transfer_type == "network":
            self.recent_network_df = df

    def reset_recent_transfers(self, transfer_type: str):
        if transfer_type == "file":
            self.recent_file_df = None
        elif transfer_type == "network":
            self.recent_network_df = None
