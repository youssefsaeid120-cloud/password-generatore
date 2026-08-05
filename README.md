# password-generatore
A simple project to make a strong passwords
# Secure Password Generator

A robust Command-Line Interface (CLI) application built with **Python** that generates highly secure, randomized passwords based on strict user-defined criteria. This project showcases strong data validation principles and precise handling of Python's built-in randomization tools.

## 🚀 Features

- **Customizable Composition**: Allows users to specify the exact count of UPPERCASE letters, lowercase letters, numbers, and symbols.
- **Strict Data Validation**: Validates user inputs dynamically, ensuring the mathematical sum of all password components perfectly matches the requested total length.
- **Infinite Retry Loop**: Keeps the application running smoothly using a `while` loop until the user provides valid inputs.
- **Enhanced Cryptographic Mixing**: Utilizes `random.shuffle()` to completely scramble the character order, eliminating predictable patterns.
- **Safe Symbol Selection**: Uses a curated list of web-safe special characters (`!@#$%^&*()_+-=`) to avoid breaking database constraints or system shells.

## 🛠️ Tech Stack & Modules Used

- **Language**: Python 3.x
- **Core Modules**:
  - `random`: Used `choices()` for repetitive picking and `shuffle()` for randomized scrambling.
  - `string`: Used `ascii_uppercase`, `ascii_lowercase`, and `digits` for clean constant character pools.

## 📂 Logic Flow

1. The script greets the user and requests the total password length.
2. It collects individual component count preferences (Caps, Small, Digits, Symbols).
3. **Validation Step**:
   - If `Total Length == Sum(Components)`, it generates, shuffles, joins the list into a string, prints it, and breaks the loop.
   - If inputs disagree, an error message is triggered, and the loop restarts.

## 💻 How to Run the Project

1. Ensure you have Python installed.
2. Clone the repository:
   ```bash
   git clone https://github.com
   ```
3. Run the script:
   ```bash
   python password_generator.py
   ```

## 📝 Future Roadmap

- [ ] Transition from `random` to the `secrets` module for cryptographically secure pseudo-random number generation (CSPRNG).
- [ ] Add a "Copy to Clipboard" feature automatically upon generation.
