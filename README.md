# Amass GUI

A graphical user interface (GUI) for OWASP Amass, developed by Alik Paranyan. This tool provides an easy-to-use interface for conducting network reconnaissance and information gathering using Amass.

## Features

- Supports both `amass intel` and `amass enum` commands.
- Easy browsing and selection of configuration files and directories.
- Real-time command execution output display.
- Comprehensive options to customize Amass commands.

## Installation

### Prerequisites

- Python 3.x
- PyQt5
- OWASP Amass

### Steps

1. **Clone the repository:**
    ```sh
    git clone https://github.com/alyaparan/amass-gui.git
    cd amass-gui
    ```

2. **Install the required Python packages:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```sh
    python amass_gui.py
    ```

## Usage

1. **Running Amass Intel:**
    - Open the "Amass Intel" tab.
    - Fill in the required fields and options.
    - Click on the "Run Amass Intel" button to execute the command.
    - The output will be displayed in the text area below.

2. **Running Amass Enum:**
    - Open the "Amass Enum" tab.
    - Fill in the required fields and options.
    - Click on the "Run Amass Enum" button to execute the command.
    - The output will be displayed in the text area below.

## Screenshot

![Amass GUI Screenshot](screenshot.png)

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Developer

**Alik Paranyan**  
Cyber Security Specialist and Cyber Criminal Enthusiast

Feel free to contact me for any questions or feedback!
