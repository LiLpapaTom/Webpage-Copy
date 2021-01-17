import urllib.request
from urllib.parse import urlparse

# Ask user for the URL
url=input("Web url to fetch:")
urlparts=urlparse(url)
if urlparts[0]=='': #equivalent would be: urlparts.scheme
    url=''.join(("http://", url))

# Ask user for the query string (part after '?')
# Leave blank if there is not any
qstring=input("Enter query string:")
if len(qstring)>0:
    url='?'.join((url,qstring))

# Ask user whether to save source code to disk or not
# If not, It will be printed to the terminal
save=input("Save downloaded page to disk [y/n]?")
print("Requesting", url)

try:
    response = urllib.request.urlopen(url)
    content = response.read()

    if save.lower()=='y':
        #Python's 3 reference for geturl():
        #Return the URL of the resource retrieved,
        #commonly used to determine if a redirect was followed
        geturl=response.geturl()
        urlparts=urlparse(geturl)
        netloc=urlparts.netloc
        if len(netloc)==0:
            fname="save.html"
        else:
            fname='.'.join((netloc,'html'))
            print('saving to',fname,'...')
            fp=open(fname,'wb')
            fp.write(content)
            fp.close()
    else:
        print(content)
except Exception as e:
    print(e.__class__.__name__,e)
