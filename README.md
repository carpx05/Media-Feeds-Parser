# Backend for Media-Feeds-Parser

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Media Supported](#media-supported)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project is the backend for the Media-Feeds-Parser, which processes and parses media feeds from various social media platforms like Instagram and Twitter.

## Project Structure
in-progress

## Media Supported
Twitter 🚧
Instagram 🚧

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Media-Feeds-Parser.git
    cd Media-Feeds-Parser
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv media-parser
    source media-parser/Scripts/activate  # On Windows use `media-parser\Scripts\activate.bat`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Configure your environment variables in the [`.env`] file.
2. Run the backend services:
    ```sh
    python Pipelines/Instagram-Service/service.py
    python Pipelines/Twitter-Service/service.py
    ```

## Configuration
- Configuration settings can be found and modified in the [`config.py`] file.
- Environment variables should be set in the [`.env`] file.

## Testing
To run tests, use the following command:
```sh
python -m unittest discover Pipelines/Twitter-Service/test.py