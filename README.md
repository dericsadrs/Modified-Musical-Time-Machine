# Deric's Musical Time Machine GUI

This Python program implements a Graphical User Interface (GUI) for Deric's Musical Time Machine. The Musical Time Machine utilizes BeautifulSoup to scrape the Billboard Top 100 for a specific date (formatted as "YYYY-MM-DD") and creates a Spotify playlist based on the scraped data.

## How it Works

1. The program displays a window with a background image and several labels to guide the user.

2. The user is asked to input a date in the format "YYYY-MM-DD" for which they want to travel back in time to create a Spotify playlist.

3. The user enters the desired date in the text field and presses the "Enter" key to submit the input.

4. The program retrieves the user's input, scrapes the Billboard Top 100 for the specified date, and creates a Spotify playlist using the scraped data.

5. If the playlist creation is successful, a "Congratulations!" message is displayed on the GUI to inform the user that the playlist has been created.

6. The user can repeat the process by entering a different date and creating additional playlists.

## Requirements

- Python 3.x
- tkinter library (included in standard Python installations)
- music_time_machine library (contains BillboardPlaylistCreator class)
- BeautifulSoup library (for web scraping)
- PIL (Python Imaging Library) library (for handling images)

## How to Use

1. Ensure that the required libraries (tkinter, BeautifulSoup, PIL) are installed.

2. Run the `MusicalTimeMachineGUI.py` script using Python.

3. The GUI window will appear, displaying the background image and labels.

4. Enter the desired date (in the format "YYYY-MM-DD") for which you want to create a Spotify playlist in the text field.

5. Press the "Enter" key or click outside the text field to submit the date.

6. The program will scrape the Billboard Top 100 for the specified date and create a Spotify playlist based on the scraped data.

7. If the playlist creation is successful, a "Congratulations!" message will be displayed on the GUI.

8. You can repeat the process by entering a different date and creating additional playlists.

## Note

- The program relies on the `BillboardPlaylistCreator` class from the `music_time_machine` library to handle the web scraping and playlist creation.

- Ensure that you have an active internet connection, as the program needs to access Billboard's website for data retrieval.

- The program will require a valid Spotify account to create playlists using the Spotify API. Make sure you have the necessary credentials set up to avoid errors during playlist creation.