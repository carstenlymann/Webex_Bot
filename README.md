# Webex_Bot

#### Chuck Norris Jokes
Chuck_Webex.py will use API to find a joke from The Internet Chuck Norris Database -> http://api.icndb.com/jokes/random

It will then post it to your chosen webex teams room, and add a Chuck Norris gif.

Run it with: python3 Chuck_Webex.py

#### Dad Jokes
DadJoke_Webex.py will use API to find a joke from icanhazdadjoke -> https://icanhazdadjoke.com/

It will then post it to your chosen webex teams room, and add a gif.

Run it with: python3 DadJoke_Webex.py


### Installation

1. Clone the repo
```sh
git clone https://github.com/carstenlymann/Webex_Bot.git
```

2. Install requirements.txt
```sh
pip3 install -r requirements.txt
```

3. Find your Webex Bearer Token and the Webex Room id where you want to receive these messages.
There is at least 3 ways that can be done
```sh
Bearer Token can be found here: https://developer.webex.com/docs/api/getting-started

Use Postman.
In postman:
	1. Get request to: https://webexapis.com/v1/rooms
	2. Under Authorization enter your Bearer Token
	3. Send
	4. Click the Body tab and find your Room id and title
	5. Copy those to the script

Use the Webex Developer site.
You can also use the developer.webex.com to find your room id.
Go to API Reference and click rooms.
You now get a list of methods regarding rooms.
Click the method GET with description List Rooms.
It has automaticly selected your bearer token, so you can just click run.
And in the response below you will have list of your rooms with title and id.

In Linux do a curl
1. sudo apt install curl <- if its not installed
2. curl -X GET -H "Autorization: Bearer ******" "https://webexapis.com/v1/rooms"
	Where ****** Is the bearer token you can find on developer.webex.com site
	The link for the request is in API Reference rooms.
	That will give you an output of all your rooms as well.. But its not easy to read..
3. curl -X GET -H "Autorization: Bearer ******" "https://webexapis.com/v1/rooms" | json_pp
	Add | json_pp to the curl, and you get a nice readable output
```

### TODO
Find special characters and format text properly.

Add skype/Microsoft Teams and email support as well.

### Misc
If you got a good idea to implement here, then let me know

If you find errors, please let me know

If you see a piece of code, that could be better, then please tell me. Im still learning

https://twitter.com/carsten_lymann
