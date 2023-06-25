from bs4 import BeautifulSoup
import requests
import lxml # lxml is a parser


URL = "https://www.amazon.com/Apple-Generation-Cancelling-Transparency-Personalized/dp/B0BDHWDR12/ref=bs_c_electronics_sccl_6/132-9243774-7791207?pd_rd_w=IQHBu&content-id=amzn1.sym.309d45c5-3eba-4f62-9bb2-0acdcf0662e7&pf_rd_p=309d45c5-3eba-4f62-9bb2-0acdcf0662e7&pf_rd_r=0M80RHBR5ZP10A30YS8E&pd_rd_wg=rilb1&pd_rd_r=6d034a5b-9ca3-4924-8af8-c5b5129bfdb6&pd_rd_i=B0BDHWDR12&psc=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(URL, headers=headers) # Get the HTML from the URL
response.raise_for_status() # Raise an exception if the status code is not 200
response_text = response.text # Get the HTML as text
soup = BeautifulSoup(response_text, "lxml") # Parse the HTML
print(soup) # Print the HTML in a readable format