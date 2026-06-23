# Password Breach Checker

A Python command-line tool that checks whether a password has appeared in a known data breach — using the [Have I Been Pwned](https://haveibeenpwned.com/Passwords) Pwned Passwords API.

## How It Works

This tool never sends your actual password over the network. Instead, it uses a privacy-preserving technique called **k-anonymity**:

1. Your password is hashed locally using SHA-1.
2. Only the **first 5 characters** of that hash are sent to the API.
3. The API returns a list of all hash suffixes that share that same 5-character prefix, along with how many times each has appeared in known breaches.
4. The script checks locally whether your full hash's suffix is in that list.

This means your real password — and even your full password hash — never leaves your machine.

## Usage

Run the script from the command line, passing one or more passwords to check:

```bash
python password_breach_checker.py password123 Tr0ub4dor&3
```

**Example output:**

```
password123 was found 2980061 times..... you should change!
Tr0ub4dor&3 was not found. Carry ON!
```

## Requirements

- Python 3.7+
- [`requests`](https://pypi.org/project/requests/)

Install the dependency with:

```bash
pip install requests
```

## Project Structure

```
password_breach_checker.py   # main script
```

## Key Functions

| Function | Purpose |
|---|---|
| `request_api_data(query_char)` | Sends the 5-character hash prefix to the Pwned Passwords API and returns the response. |
| `get_password_leaks_count(hashes, hash_to_check)` | Searches the API response for a matching hash suffix and returns its breach count. |
| `pwned_api_check(password)` | Hashes the password (SHA-1), splits it into prefix/suffix, and runs the full check. |
| `main(args)` | Loops through all passwords passed via the command line and prints the result for each. |

## Why I Built This

I wanted a quick, practical way to check passwords against real breach data without relying on a website — and to understand how privacy-conscious APIs like this one are designed. The same core logic also powers a live browser-based version of this tool on my portfolio site, built with JavaScript and the Web Crypto API.

## License

This project is open source and available for personal and educational use.

## Author

**Ridwan Ibrahim**
Python Developer · Software Engineer 
[LinkedIn](https://www.linkedin.com/in/ridwan-ibrahim-8547b1154/)
