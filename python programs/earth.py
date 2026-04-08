import webbrowser

def open_google_earth():
    """Opens Google Earth in the system's default web browser."""
    url = 'https://google.com'
    
    try:
        # Returns True if a browser is successfully launched
        if webbrowser.open(url):
            print(f"Successfully opened: {url}")
        else:
            print("Failed to open browser.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    open_google_earth()
