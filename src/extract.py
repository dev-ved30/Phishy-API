from urllib.parse import urlparse
import requests

features = {
    "having_IP_Address": 0,
    "port": 0,
    "URL_Length": 0,
    "having_At_Symbol": 0,
    "double_slash_redirecting": 0,
    "Prefix_Suffix": 0,
    "Redirect": 0,
    "HTTPS_token": 0,
    "Shortining_Service": 0,
    "having_Sub_Domain": 0,
    "having_IP_Address": 0,
}

ports = {
    "http": 80,
    "https": 443,
    "ftp": 21,
    "ssh": 22,
    "telnet": 23,
    "smb": 445,
    "mssql": 1433,
    "oracle": 1521,
    "mysql": 3306,
    "remotedesktop": 3389
}

def extractPort():
    port = ports[elements.scheme]
    ## Wait till we implement pure URL features

def extractUrlLength():
    """
    Sets the URL_Length feature with the threshold value of 54.

    1) -1 if the length is greater than or equal to 54.
    2) 1 if the length is less than 54.
    """

    if (len(URL) >= 54 ):
        features['URL_Length'] = -1
    else:
        features['URL_Length'] = 1

def extractAtSymbol():
    """
    Sets the having_At_Symbol feature based on the presence of @ in the URL

    1) -1 if the URL contains @
    2) 1 if the URL does not contain @
    """

    if "@" in URL:
        features["having_At_Symbol"] = -1
    else:
        features["having_At_Symbol"] = 1

def extractDoubleSlashRedirecting():
    """
    Sets the double_slash_redirecting feature based on the position of the last //.

    1) -1 if the last occuring // is after the 6th index.
    2) 1 if the last occuring // is before the 6th index.
    """
    
    if URL.rfind("//") > 6:
        features["double_slash_redirecting"] = -1
    else:
        features["double_slash_redirecting"] = 1

def extractPrefixSuffix():
    """
    Sets the Prefix_Suffix feature after checking if the domain(netloc) comtains a -.

    1) -1 if the domain(netloc) contains a -.
    2) 1 if the domain(netloc) does not contain a -.
    """

    if '-' in elements.netloc:
        features["Prefix_Suffix"] = -1
    else:
        features["Prefix_Suffix"] = 1

def extractRedirects():
    """
    Sets the Redirect feature after checking if the URL redirects to a different URL.

    1) -1 if more than one redirects take place.
    2) 1 if less than or equal to 1 redirects take place.
    """

    responses = requests.get(URL, allow_redirects=True)
    if len(responses.history) > 1:
        features["Redirect"] = -1
    else:
        features["Redirect"] = 1

def extractHttpsToken():
    """
    Sets the HTTPS_token feature after checking if the domain starts with https or http.

    1) -1 if the domain begins with https or http.
    2) 1 if the domain does not begin with https or http.
    """
    if elements.netloc.startswith("https") or elements.netloc.startswith("http"):
        features["HTTPS_token"] = -1
    else:
        features["HTTPS_token"] = 1

def extractShortiningService():
    """
    Sets the Shortining_Service feature after checking if the domain starts with one of the popular link shortening websites.

    1) -1 if the domain begins with a link shortening domain.
    2) 1 if the domain does not begin with a link shortening domain.
    """

    if elements.netloc.startswith(("bit.ly", "t.co", "tinyurl")):
        features["Shortining_Service"] = -1
    else:
        features["Shortining_Service"] = 1

def extractHavingSubDomain():
    """
    Sets the having_Sub_Domain feature after checking how many sub-domains the hostname has.
    This number include the "www." prefix and the top level domain like ".com" or ".uk"

    1) -1 if the hostname has more than 3 parts after splitting along '.' ie "www." + some name + ".com". 
    2) 1 if the hostname has 3 or fewer parts after splitting along '.'
    """

    list = elements.hostname.split(".")
    if len(list) > 3:
        features["having_Sub_Domain"] = -1
    else:
        features["having_Sub_Domain"] = 1

def extractHavingIpAdress():
    """
    Sets the having_IP_Address feature after checking if the domain resembles an IP adress.

    1) -1 if the domain resembles an IP Address in integer or hexadecimal form.
    2) 1 if the domain does not resemble an IP Address in integer or hexadecimal form.
    """

    parts = elements.netloc.split('.')

    # Number of times a number appears in the domain
    countNum = 0
    # Numver of times a hexadecimal appears in the domain
    countHex = 0
    # Number of times a 'Normal' string appears in the domain
    countNormal = 0

    for part in parts:
        if part.isdigit():
            countNum = countNum + 1
        else:
            try:
                int(part, 16)
                countHex = countHex + 1
            except ValueError:
                countNormal = countNormal + 1
    
    if countNum + countHex > 0:
        features["having_IP_Address"] = -1
    else:
        features["having_IP_Address"] = 1

def extractAllFeatures(url):
    global URL 
    global elements
    URL = url
    elements = urlparse(URL)
    extractPort()
    extractAtSymbol()
    extractUrlLength()
    extractDoubleSlashRedirecting()
    extractPrefixSuffix()
    extractRedirects()
    extractHttpsToken()
    extractShortiningService()
    extractHavingSubDomain()
    extractHavingIpAdress()
    extractHavingIpAdress()
    print(features)
    return features

link = "https://www.youtube.com/watch?v=8OpMAlYyH5Y"
extractAllFeatures(link)