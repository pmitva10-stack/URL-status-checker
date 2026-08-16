# URL Status Checker

A small Python script that checks whether a list of websites are reachable by sending a GET request to each one and printing the HTTP status code.

## What it does

- Loops through a list of URLs (Google, Wikipedia, YouTube, GitHub)
- Sends a `GET` request to each using the `requests` library
- Prints the HTTP status code if the request succeeds
- Prints a message if the site is unreachable (e.g. connection error, timeout)

## What I learned

Some sites returned a `403 Forbidden` error when the request was sent without a `User-Agent` header. This happens because many servers block requests that look like they're coming from a script/bot rather than a real browser — Python's `requests` library sends a default `User-Agent` like `python-requests/x.x.x`, which is an easy signal for servers to detect and reject.

Fix: manually set a `User-Agent` header that mimics a real browser (e.g. Chrome on Windows), which was enough to get past the block:

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
```

## How to run

1. Install the `requests` library if you don't already have it:
   ```
   pip install requests
   ```
2. Run the script:
   ```
   python url_checker.py
   ```
3. The script will print a status code (like `200`) for each reachable URL, or a message noting that the URL is unreachable.
