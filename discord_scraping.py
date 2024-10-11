import requests
from bs4 import BeautifulSoup

with open('urls.txt', 'r') as file:
    urls = file.readlines()

urls = urls[19000:19400]
# Print the lines
for url in urls:
    print(url.strip())  # strip() removes the newline characters
    url = url.strip()
    



    # URL of the page to scrape
    # url = 'https://coinmarketcap.com/currencies/wagmi-com/'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the title of the page
        
        # Find all hyperlinks in the page
        links = soup.find_all('a')
        
        # Print all links
        for link in links:
            href = link.get('href')
            text = link.get_text()
            # if "discord" in href:
            #     print(f'Link text: {text}, URL: {href}')
            if href and "discord" in href:
                print(href)
                with open('discord_urls.txt', 'a') as file:
                    # Write the string to the file
                    file.write(href + "\n")
            if href and "t.me" in href:
                print(href)
                with open('telegram_urls.txt', 'a') as file:
                    # Write the string to the file
                    file.write(href + "\n")
    else:
        print(f'Failed to retrieve the page. Status code: {response.status_code}')

