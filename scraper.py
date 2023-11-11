import re
from urllib.parse import urlparse

def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]


def extract_next_links(url, resp):
    # Check if the response status is valid (e.g., 200 OK)
    if resp.status == 200:
        # Initialize an empty list to store URLs
        urls_to_crawl = [
    "http://ics.uci.edu/",
    "http://cs.uci.edu/",
    "http://informatics.uci.edu/",
    "http://stat.uci.edu/"]


      # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(resp.raw_response.content, 'html.parser')

        # Find and extract links from the page
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                # Check if the URL meets the criteria for further crawling
                if is_valid(href):
                    urls_to_crawl.append(href)

        return urls_to_crawl

    # Return an empty list for non-200 responses
    return []

def is_valid(url):
    try:
        parsed = urlparse(url)
        # Check if the URL scheme is either 'http' or 'https'
        if parsed.scheme not in set(["http", "https"]):
            return False

        # Define a list of file extensions to filter out
        invalid_extensions = [
            "css", "js", "bmp", "gif", "jpeg", "jpg", "ico",
            "png", "tiff", "mid", "mp2", "mp3", "mp4",
            "wav", "avi", "mov", "mpeg", "ram", "m4v", "mkv", "ogg", "ogv", "pdf",
            "ps", "eps", "tex", "ppt", "pptx", "doc", "docx", "xls", "xlsx", "names",
            "data", "dat", "exe", "bz2", "tar", "msi", "bin", "7z", "psd", "dmg", "iso",
            "epub", "dll", "cnf", "tgz", "sha1", "thmx", "mso", "arff", "rtf", "jar", "csv",
            "rm", "smil", "wmv", "swf", "wma", "zip", "rar", "gz"]

            # Check if the URL path ends with any of the invalid extensions
        if any(url.endswith("." + ext) for ext in invalid_extensions):
                return False

            # Add custom filtering rules here, if needed

            # If the URL passes all checks, it is considered valid
        return True

    except Exception:
        # Handle exceptions gracefully, e.g., for invalid URLs
        return False
