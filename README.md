# Password Manager

A simple desktop application built with Python and Tkinter to manage passwords. It allows users to generate strong passwords, save login credentials for websites, and retrieve them later. The application stores data in a JSON file and includes a feature to copy generated passwords to the clipboard.

## Features
- **Password Generation**: Creates random, secure passwords with a mix of letters, numbers, and symbols.
- **Password Storage**: Saves website credentials (website name, email/username, and password) to a JSON file.
- **Search Functionality**: Retrieves stored credentials for a specified website.
- **Clipboard Support**: Automatically copies generated passwords to the clipboard.
- **User-Friendly Interface**: Built with Tkinter for a simple and intuitive GUI.

## Requirements
- Python 3.x
- Tkinter (included with standard Python installation)
- `pyperclip` library (`pip install pyperclip`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-manager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-manager
   ```
3. Install the required dependencies:
   ```bash
   pip install pyperclip
   ```
4. Ensure you have the `logo.png` file in the project directory for the application logo. (Replace with your own logo or remove the logo-related code if not needed.)

## Usage
1. Run the application:
   ```bash
   python main.py
   ```
2. **Generate a Password**:
   - Click the "Generate" button to create a random password.
   - The password will be inserted into the password field and copied to the clipboard.
3. **Save Credentials**:
   - Enter the website name, email/username, and password.
   - Click the "Add" button to save the credentials to `data.json`.
   - Ensure all fields are filled to avoid errors.
4. **Search Credentials**:
   - Enter the website name and click the "Search" button to retrieve saved credentials.
   - A message box will display the email and password if found, or an error if the website is not in the database.
5. **View Stored Data**:
   - Credentials are stored in `data.json` in the project directory.

## File Structure
- `main.py`: The main Python script containing the application logic.
- `logo.png`: The logo image displayed in the GUI (ensure it exists or modify the code to remove this dependency).
- `data.json`: Automatically created to store credentials (generated when saving data).

## Notes
- The application requires a `logo.png` file in the project directory. If you don't have one, you can remove the logo-related code in `main.py` (lines related to `PhotoImage` and `canvas.create_image`).
- The `data.json` file is created automatically when you save credentials for the first time.
- Ensure you have write permissions in the project directory to create and modify `data.json`.

## Example
1. Launch the application.
2. Enter a website (e.g., "example.com"), email/username (e.g., "user@example.com"), and click "Generate" to create a password.
3. Click "Add" to save the credentials.
4. To retrieve, enter the website name and click "Search" to view the saved email and password.

## Contributing
Feel free to submit issues or pull requests to improve the application. Suggestions for additional features or bug fixes are welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.