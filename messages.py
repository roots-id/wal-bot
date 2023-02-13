
BOT_CONNECT_MSG = """is connected to the following guilds:\n"""

WELCOME_MSG = """Hello!

Thank you for using WAL-BOT. Our bot is designed to demonstrate how decentralized identity can be used to create verifiable credentials. Essentially, this means that we can take the metadata associated with your Discord account (such as your username, avatar, and any other information you have provided) and create a digital certificate that can be used to verify your identity online.

Please note that this verifiable credential does not have any practical utility at this time. It is simply an example of how decentralized identity can be used in practice. However, we hope that by showcasing the capabilities of decentralized identity, we can encourage more widespread adoption of this technology and its potential applications.

Thank you again for using WAL-BOT, and we hope you enjoy learning more about decentralized identity!"""

HELP_CMD_MSG = """Type /help for a list of commands."""

WELCOME_CMD_MSG_S = """Get the welcome message from the bot"""
WELCOME_CMD_MSG_L = """Get the welcome message from the bot."""

INFO_CMD_MSG_S = """Shows the discord user information"""
INFO_CMD_MSG_L = """Shows the discord user information that will be included in the credential."""

ISSUE_CMD_MSG_S = """Get your verifiable Discord credential (QR Code)"""
ISSUE_CMD_MSG_L = """To request a verifiable Discord credential, send a direct message to the bot with the command "/issue" followed by your email address (optional). For example:

/issue none@example.com

After calling this command, the bot will display a QR code that you will need to scan with the RootsWallet mobile application. Once you have scanned the QR code, the credential issuance process will begin.

Please note that you will need to have the RootsWallet app installed on your mobile device in order to complete this process. You can download the app for free from the App Store or Google Play Store."""

ISSUE_MSG = """Scan the QR code below with the RootsWallet mobile application to get your verifiable Discord credential."""

ISSUE_URL_CMD_MSG_S = """Get your verifiable Discord credential (URL Invitation)"""
ISSUE_URL_CMD_MSG_L = """To request a verifiable Discord credential, send a direct message to the bot with the command "/issue_url" followed by your email address (optional). For example:

/issue_url none@example.com

After calling this command, the bot will display a URL that you will need to accept with your PRISM Agent. Once you have accepted the invitation, the credential issuance process will begin.

Please note that you will need to have access to a PRISM Agent in order to complete this process."""

ISSUE_URL_MSG = """Use the invitation URL with your PRISM Agent to get your verifiable Discord credential."""

ISSUE_PARAM_EMAIL_DESC = """- your email address"""
ISSUE_PARAM_EMAIL_DEFAULT = """none@example.com"""
