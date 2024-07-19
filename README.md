# TCP Reverse Shell from scracth using Python

This repository contains a TCP reverse shell implementation developed for educational and research purposes. The tool is designed to demonstrate concepts in network programming, system security, and encryption.

## Disclaimer

**WARNING**: This tool is intended for educational purposes only. The use of this software for malicious activities is illegal and unethical. The author does not condone or support any illegal activities. By using this software, you agree to use it responsibly and within the bounds of the law. The author assumes no liability for any misuse of this software.

## Features

- Establishes a reverse TCP connection from a client to a server.
- Uses AES encryption to secure communication.
- Supports multiple client connections.
- Allows the server to remotely execute commands on the client machine.
- The client program automatically starts on system boot.
- Bypasses basic antivirus detection mechanisms.

## Usage

### Server (Handler)

The server listens for incoming connections from clients and provides an interactive shell to send commands to connected clients.

#### Setup

1. Ensure you have Python installed on your system.
2. Install the required dependencies:
   ```bash
   pip install pycryptodomex
   ```
3. Run the server script:
   ```bash
   python multi_attacker.py
   ```

### Client (Victim)

The client connects to the server and waits for commands to execute.

#### Setup

1. Ensure you have Python installed on the victim's system.
2. Install the required dependencies:
   ```bash
   pip install pycryptodomex
   ```
3. Run the client script on the victim machine:
   ```bash
   python victim.py
   ```

### Commands

- **list**: Lists all connected clients.
- **select [index]**: Selects a client to interact with.
- **quit**: Exits the shell.

## Encryption

Communication between the server and the client is encrypted using AES (Advanced Encryption Standard) with a predefined key and initialization vector (IV). This ensures that data transferred between the server and client is not easily readable by third parties.

## Educational Purpose

The primary goal of this project is to provide a practical example of:

- Network programming using Python's `socket` library.
- Implementing AES encryption for secure communication.
- Developing a multi-threaded application to handle multiple client connections.

By studying and experimenting with this code, learners can gain insights into how reverse shells work and how encryption can be used to secure communication channels.

## Legal and Ethical Considerations

It is crucial to understand the ethical implications of developing and using tools like reverse shells. Such tools can be used for malicious purposes, and it is your responsibility to ensure that you use this knowledge and software ethically and legally. Always obtain explicit permission before running this software on any system.

## Conclusion

This project is a powerful learning tool for those interested in network security and ethical hacking. Use it responsibly, and always prioritize ethical considerations in your work.

## Contact

For any questions or concerns, please contact the author at [harshnkgupta@gmail.com].
