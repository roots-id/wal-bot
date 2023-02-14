# wal-bot
This project works together with [discord-controller](https://github.com/roots-id/discord-controller) to implement the Discord Social Credential use case.

The purpose of the project is to demonstrate how decentralized identity can be used to create verifiable credentials. Essentially, this means that we can take the metadata associated with your Discord account (such as your username, avatar, and any other information you have provided) and create a digital certificate that can be used to verify your identity online.

Please note that this verifiable credential does not have any practical utility at this time. It is simply an example of how decentralized identity can be used in practice. However, we hope that by showcasing the capabilities of decentralized identity, we can encourage more widespread adoption of this technology and its potential applications.

## Setup

Clone this repo
```
python -m venv venv
``` 

Activate python venv 

On Windows, run:
```
cd venv
venv\Scripts\activate.bat
```
On Unix or MacOS, run:
```
cd venv
source venv/bin/activate
```

Set DISCORD_TOKEN environment variable
Windows
```
setx DISCORD_TOKEN <token> /m
```
Linux/MacOS (TODO add instructions for bashrc)
```bash
export DISCORD_TOKEN=<token>
```
### Requirements
python -m pip install -r requirements.txt
