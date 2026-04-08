import webbrowser
from urllib.parse import quote

def open_google_earth(search_query=None):
    """
    Opens Google Earth. 
    If search_query is provided, it opens that specific location.
    """
    base_url = "https://earth.google.com/"
    
    if search_query:
        # Properly encode the search term for a URL (e.g., "Grand Canyon" -> "Grand%20Canyon")
        url = f"{base_url}search/{quote(search_query)}"
    else:
        url = base_url

    try:
        # Open in the system's default browser (ie. Chrome 146)
        if webbrowser.open(url):
            print(f"Successfully launched Google Earth for: {search_query if search_query else 'Home'}")
        else:
            print("Could not open the browser.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    open_google_earth()
