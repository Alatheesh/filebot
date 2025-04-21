# Telegram File Forwarder Bot

This Telegram bot, deployed on Koyeb, allows users to request a file by name, and the bot will forward that file from a specified Telegram channel where it has administrator privileges.

## Setup

1.  **Prerequisites:**
    * A Telegram bot token (obtained from BotFather).
    * The numerical ID of the Telegram channel where the files are located. The bot must be an administrator in this channel.
    * A Koyeb account.
    * A GitHub account.

2.  **Repository Setup:**
    * Clone this repository to your local machine.
    * Ensure you have Python installed.
    * Install the required Python library:
        ```bash
        pip install -r requirements.txt
        ```
    * **Do not hardcode your bot token or channel ID in the `main.py` file.** These will be configured as environment variables on Koyeb.

## Deployment to Koyeb

1.  Create a new app on Koyeb and connect it to this GitHub repository.
2.  Configure the following environment variables in your Koyeb app settings:
    * `BOT_TOKEN`: Your Telegram bot token.
    * `SOURCE_CHANNEL_ID`: The numerical ID of the source Telegram channel.
3.  Koyeb will automatically build and deploy your bot.

## Usage

1.  Start a chat with your bot on Telegram.
2.  Use the `/start` command to get a welcome message.
3.  Send the exact name of the file you want to retrieve.
4.  The bot will forward the file to you if it's found in the specified source channel.

## Important Notes

* The bot performs an exact match on file names.
* For large channels, searching the entire history might take time. Consider alternative approaches for better performance in such cases.
* Ensure your bot has the necessary permissions in the source channel to read messages.
