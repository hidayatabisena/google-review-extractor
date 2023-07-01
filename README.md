
# Google Review Extractor

The Google Reviews Extractor is a Python script designed to help you gather valuable feedback for your friend's business. It allows you to extract the top 50 newest Google reviews for specific places using the Google Places API.

By utilizing this script, you can easily retrieve and display the most recent reviews for your friend's business, providing insights into customer experiences and enabling data-driven improvements.


## Screenshots

![Window Screenshot](https://res.cloudinary.com/moyadev/image/upload/v1688212295/Moyadev/CleanShot_2023-07-01_at_18.26.56_2x_x4wurx.png)


## Features

- Retrieve the top 50 newest Google reviews for a specified place
- Display review details such as rating, author, and review text
- Securely store your Google Places API key using the python-dotenv package
- Simple and easy-to-understand code structure
- Customizable and extendable for further enhancements or integrations


## Getting Started

1. Obtain a Google Places API key by creating a project in the [Google Cloud Console](https://console.cloud.google.com/)
2. Install the required dependencies by `running pip install -r requirements.txt`
3. Create a `.env` file in the project directory and add your API key as `API_KEY=your_api_key`
4. Run the script and enter the name of the place you want to extract reviews for
5. The script will retrieve and display the top 50 newest reviews for the specified place


## Dependencies

- requests: for making HTTP requests to the Google Places API
- python-dotenv: for securely storing and accessing the API key from a `.env` file.


## Notes

- Ensure you have an internet connection to access the Google Places API
- Take into account the usage limits of the Google Places API and consider enabling billing for larger-scale usage
- Remember to keep your API key secure and avoid exposing it in public repositories


## Improvements idea

- **Pagination Support**: Currently, the script retrieves the top 50 newest reviews. To handle cases where there are more than 50 reviews available, you can implement pagination support to fetch additional pages of reviews and display a larger number of results

- **Sorting Options**: Enhance the script to allow sorting the reviews based on different criteria such as rating, date, or relevance. This feature would provide flexibility in analyzing and presenting the reviews according to specific requirements

- **Sentiment Analysis**: Consider integrating a sentiment analysis library or API to automatically analyze the sentiment of the reviews. This enhancement would provide insights into the overall sentiment of customer feedback and enable automatic categorization of positive, negative, or neutral reviews

- **Data Visualization**: Extend the script to generate visualizations such as charts or graphs to present a summary of review ratings and sentiment distribution. This visual representation can help in quickly understanding the overall feedback and identifying trends

- **User Interface**: Develop a user-friendly graphical interface or web application that allows users to interact with the script easily. This enhancement would eliminate the need for running the script directly from the command line and provide a more intuitive way to input the place name and view the extracted reviews

- **Multi-platform Support**: Adapt the script to work on different platforms such as Windows, macOS, and Linux. This modification would ensure that the script can be used across various operating systems without any compatibility issues

- **Export Results to CSV**: Add functionality to export the retrieved reviews to a CSV (Comma-Separated Values) file. This feature would enable you to save the review data in a structured format that can be easily imported into spreadsheet software for further analysis or reporting

- **Error Handling and Logging**: Implement comprehensive error handling and logging mechanisms to gracefully handle potential errors and exceptions during API requests. This improvement would make the script more robust and aid in troubleshooting and debugging


## Authors

- [Han Sena](https://www.github.com/hidayatabisena)


## Tech Stack

**CLI:** Python

