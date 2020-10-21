import requests

##########################
### Get the Chuck Joke ###
##########################

url = "http://api.icndb.com/jokes/random"

chuck = requests.get(url)

# Print the Joke for test purpose
#print(chuck.json()["value"]["joke"])

# Making a variable with just the joke from the chuck return
chuck_joke = (chuck.json()["value"]["joke"])

# For testing
#print(chuck_joke)

####################################
### Post the Joke to Webex teams ###
####################################

url = "https://webexapis.com/v1/messages"


gif = "https://media.giphy.com/media/7qZ3ZX1Gu3TZm/giphy.gif"


# Find your room id.
# I used postman for that. Make a GET to https://webexapis.com/v1/rooms and enter your Bearer token under authorization
# You should now get a list of your rooms, including room ID for each of them.
# Take that ID and replace ***** below in var_roomid variable to your ID
# Authorization need to be found here: https://developer.webex.com/docs/api/getting-started

var_roomid = '\"*****\"'
var_array = '\r\n'
var_navn = ''.join(('"', chuck_joke, '"'))
var_file = ''.join(('[\"', gif, '"]'))

payload = "{" + var_array + "  \"roomId\": " + var_roomid + "," + var_array + "  \"text\": " + var_navn + "," + var_array + "  \"files\": " + var_file + "\r\n}"

# Test print
#print(payload)

# Use same Authorization as used in postman to get room id.
# Take title of your room, and replace >>>> below
# Put in after Bearer instead of the ******

headers = {
    'title': ">>>>>",
    'Content-Type': "application/json",
    'Authorization': "Bearer ******", #Found here: https://developer.webex.com/docs/api/getting-started
    'cache-control': "no-cache"   
    }

response = requests.request("POST", url, data=payload, headers=headers)

#print(response.text)
