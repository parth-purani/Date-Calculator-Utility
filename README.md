# 📅 Python Date Calculator Utility

This Python script offers a handy utility for calculating the next and previous dates from a given date, formatted as YYYY-MM-DD. It features a user-friendly command-line interface for easy date manipulation.

## 🛠 Components and Functionalities

### 📝 Functions

- **after(date: str) -> str**: Computes and returns the date following the specified date.
- **before(date: str) -> str**: Computes and returns the date before the specified date.

### 🔁 Main Loop

- Provides a menu-driven interface, allowing users to select operations to compute the next date, the previous date, or exit the program.

## 🌟 Features

### Date Calculation Logic

- **Leap Year Calculation**: Adjusts February's days in leap years based on divisibility by 4, 100, and 400.
- **Month Handling**: Manages the varying number of days across months, ensuring accurate transitions (e.g., December to January).
- **Edge Cases**: Ensures correct date calculations during year and month transitions.

### User Input and Validation

- Ensures dates are input in the correct YYYY-MM-DD format. If incorrect, returns '0000-00-00'.
- Continually prompts for user input, enhancing interaction until the exit option is selected.

## 🚀 Example Usage

Upon execution, the script displays:

```markdown
1. After date
2. Before date
3. Exit
