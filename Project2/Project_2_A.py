import urllib.request
import re

# User input search query
search_query = input("Enter your search query: ")

# parse search query
encoded_query = urllib.parse.quote(search_query)

# Construct URL
url = f"https://www.google.com/search?q={encoded_query}"

# Set the User-Agent header to bypass google script dectection
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}

# Create a Request object with the URL and headers
request = urllib.request.Request(url, headers=headers)

# Perform the HTTP request to the search engine
with urllib.request.urlopen(request) as response:
    html = response.read().decode("utf-8")

# Extract the titles of the top 10 search results using regular expressions
titles = re.findall(r'<h3 class=".*?">(.*?)</h3>', html)[:10]

# Display the titles to the user
print("Top 10 Search Results:")
for title in titles:
    print(title)
