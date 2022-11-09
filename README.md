# wal-bot
Discord Bot for Social Credential PoC

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

### Misc notes

[Why is not possible to get email from discord account](https://www.itgeared.com/how-to-get-someones-email-from-discord/#:~:text=To%20access%20it%2C%20open%20your,email%20associated%20with%20your%20Discord.)

