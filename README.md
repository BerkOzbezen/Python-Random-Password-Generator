# 🔑 Strong Random Password Generator (Python)

This is a simple yet robust command-line application built in Python that generates strong, randomized passwords.

## ✨ Features

- **Guaranteed Strength:** Ensures the inclusion of at least one uppercase letter, one lowercase letter, one digit, and one special character.
- **Variable Length:** Allows the user to specify the desired password length (minimum 4).
- **Default Length:** Automatically generates a 12-character password if no length is specified.
- **Unpredictable:** Utilizes the `random.shuffle` method to randomize the position of guaranteed characters.

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/BerkOzbezen/Python-Random-Password-Generator]
    cd Python-Random-Password-Generator
    ```

2.  **Execute the script:**
    ```bash
    python password_generator.py
    ```

## 🛠️ Usage

When you run the script, you will be prompted to enter the desired password length:

Enter the desired password length (minimum 4, press Enter for 12) :
| Input | Result |
| :--- | :--- |
| **16** | Generates a 16-character strong password. |
| **[Enter]** | Generates the default 12-character strong password. |
| **3** | Raises a `ValueError` (Error due to minimum length constraint). |

## ⚙️ Dependencies

This script uses only Python's standard library modules:
- `random`
- `string`

## 👨‍💻 Author

- [Berk Özbezen / BerkOzbezen]