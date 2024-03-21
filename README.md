# Embed Bot

Embed Bot is a Discord bot designed to enhance your Discord experience by embedding videos directly within your server's text channels. It supports content from popular platforms like TikTok, Instagram, Twitter, and iFunny, making it easier for users to share and view content without leaving Discord.

## Features

- **Video Embedding**: Automatically embeds videos from TikTok, Instagram, Twitter, and iFunny.
- **Easy Sharing**: Users can share videos by simply pasting the video link in the text channel.
- **Cross-Platform Support**: Designed to work seamlessly across multiple content platforms.

## Getting Started

These instructions will help you get a copy of Embed Bot up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have Python 3.6 or later installed on your system. This bot relies on Python's asynchronous features and external libraries that may not be compatible with older versions of Python.

### Installation

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```sh
   git clone https://github.com/x2dtu/embed_bot.git
   cd embed_bot
   ```

2. **Get a Discord Client Bot Token**
   Once this is obtained (look at discord documentation for how to get this), either export it as an environment variable named `DISCORD_SECRET` or replace the `os.getenv('DISCORD_SECRET')` with the string key in the final line of `discord_boy.py`

3. **Run Build Script**

   To simplify the build process, a `build.sh` script is provided. This script automates the creation of a virtual environment installation of dependencies, setup of Playwright, and starting the bot. Run the following command in the terminal (assuming you have mac or linux):

   ```sh
   ./build.sh
   ```

   This script performs the following actions:

   - Creates a .venv virtual environment in your project directory.
   - Installs all required dependencies listed in requirements.txt.
   - Runs playwright install to set up Playwright, which is essential for video embedding functionality.
   - Starts the Discord bot.

   For windows, you can follow the lines in the `build.sh` script, but need to replace the `.venv/bin/activate` line with `.\.venv\Scripts\activate`

4. **Running the Bot**
   After running the `build.sh` script, your bot should be up and running. Make sure to configure your bot token from step 2.
