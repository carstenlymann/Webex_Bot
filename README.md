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

3. Find your Webex Bearer Token and the Webex Room id where you want to receive these messages
```sh
Bearer Token can be found here: https://developer.webex.com/docs/api/getting-started

I used Postman to find my room id
In postman:
	1. Get request to: https://webexapis.com/v1/rooms
	2. Under Authorization enter your Bearer Token
	3. Send
	4. Click the Body tab and find your Room id and title
	5. Copy those to the script
```

### TODO
Find special characters and format text properly.

Add skype/Microsoft Teams and email support as well.

### Misc
If you got a good idea to implement here, then let me know

If you find errors, please let me know

If you see a piece of code, that could be better, then please tell me. Im still learning

https://twitter.com/carsten_lymann
