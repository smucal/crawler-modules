import requests

response = requests.get('https://github.com')

print(response.content)


# from bs4 import BeautifulSoup

# Here, we're just importing both Beautiful Soup and the Requests library
# this is the url that we've already determined is safe and legal to scrape from.

# # here, we fetch the content from the url, using the requests library
# page_content = BeautifulSoup(page_response.content, "html.parser")
# #we use the html parser to parse the url content and store it in a variable.
# textContent = []
# for i in range(0, 20):
#     paragraphs = page_content.find_all("p")[i].text
#     textContent.append(paragraphs)
# # In my use case, I want to store the speech data I mentioned earlier.  so in this example, I loop through the paragraphs, and push them into an array so that I can manipulate and do fun stuff with the data.