# Transfers (Molex AI Model)

This project is a file transfer system developed in Python. It allows for both local file transfers and network file transfers.

## Features

- **Local File Transfers**: This feature allows for transferring files or directories from one local directory to another. It checks if the source is a directory. If it is, it copies the entire directory to the destination. If it's not, it proceeds with the file transfer process.

- **Network File Transfers**: This feature allows for transferring files over a network. It opens a socket connection to the destination IP and port, reads the source file in binary mode, and sends the file data over the socket connection.

- **Duplicate Check**: Before transferring, the system checks for duplicates in the source directory list.

- **Predictions**: The system includes a `Predict` class that can be used to make predictions based on the recent transfers.

## Installation

To install the project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies.

## Usage

To use the project, follow these steps:

1. Import the necessary modules.
2. Call the `transfer_files` or `transfer_files_over_network` function with the appropriate dataframe.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

## License

This project is licensed under the terms of the MIT license.
