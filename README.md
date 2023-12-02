# Knock Knock - Port Scanner

## Description

Knock Knock is a simple and customizable port scanning tool written in Python. It combines the concept of port knocking with port scanning to enhance network security. The tool performs a sequence of connection attempts (port knocking) before scanning the specified range of ports on a target system to identify open ports.

### Installation

1. Clone the repository:

   - git clone https://github.com/yourusername/knockknock.git

   - cd knockknock

2. Install the required dependencies:

   - pip install -r requirements.txt

### Usage

Create a text file containing a list of target IP addresses, one per line.

#### Run the script:
python knockknock.py

Follow the prompts to provide the path to the IP addresses file, the range of ports to scan, and any other required inputs.

The tool will perform port knocking using the specified sequence and then scan the target ports for each IP address. The results will be saved in separate text files for each IP address in the current working directory.

#### Real-time Results:
As the tool progresses, real-time results are saved in separate text files named realtime_results_{ip}.txt in the current directory.

#### Note:
Ensure that you have Python installed on your system.
Adjust the knock_sequence and other parameters in the script according to your requirements.
Author: MrMagic0

#### Disclaimer:
This tool is intended for educational and security testing purposes only. Use it responsibly and only on systems that you have explicit permission to test.
