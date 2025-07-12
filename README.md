# MyPass - Password Manager

A simple password manager application built with Python using the `tkinter` library. This tool allows you to generate secure passwords and save them along with website and email/username details to a text file. The interface features a lock-themed logo for a secure feel.

## Project Structure

- **main.py**: Contains the core logic for password generation, saving credentials, and UI setup.
- **logo.png**: The lock image used as the application logo (ensure it’s in the project directory).

## Prerequisites

To run the application, you need Python installed along with the following libraries:

- `tkinter` (standard library, included with Python)
- `pyperclip` (for copying generated passwords to the clipboard)

Install `pyperclip` using pip:

```bash
pip install pyperclip
```

Ensure the `logo.png` image file is present in the project directory (as used in the code for the canvas display).

## How to Run

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd mypass
   ```

3. Ensure the `logo.png` image file is in the directory (replace it with your own lock image if needed, matching the canvas size of 200x200 pixels).

4. Install the required library:

   ```bash
   pip install pyperclip
   ```

5. Run the application:

   ```bash
   python main.py
   ```

## Features

- **Password Generator**: Creates a random password with 8-10 letters, 2-4 symbols, and 2-4 numbers, then copies it to the clipboard.
- **Save Credentials**: Stores website, email/username, and password details in `data.txt`.
- **Validation**: Checks for empty fields and prompts for confirmation before saving.
- **User Interface**: Includes input fields for website, email/username, and password, with buttons for generating and saving passwords.

## Usage

- Enter the website name in the "Website" field.
- Enter or use the default "example@gmail.com" in the "Email/Username" field (editable).
- Click "Generate" to create a random password, which auto-fills the password field and is copied to your clipboard.
- Click "Add" to save the details to `data.txt` after confirming via a pop-up.
- The fields clear after a successful save, ready for the next entry.

## File Descriptions

- **main.py**: Implements the password manager functionality, including:
  - Password generation using random selection and shuffling.
  - Saving credentials to `data.txt` with validation and user confirmation.
  - UI setup with `tkinter`, featuring a canvas for the logo and input fields/buttons.

- **data.txt**: A text file where saved credentials are stored in the format `website | email | password` (one entry per line).

- **logo.png**: The lock image displayed in the UI (must be 200x200 pixels).

## Notes

- The generated passwords are copied to the clipboard automatically for convenience.
- Saved data is appended to `data.txt` in plain text; consider encrypting it for security in a production environment.
- The `logo.png` file must be in the same directory as `main.py` to load correctly.
- This is a basic implementation; for real-world use, enhance security with encryption and a database.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the existing style and includes appropriate comments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.