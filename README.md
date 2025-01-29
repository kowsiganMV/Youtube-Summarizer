# YouTube Summarizer

## Overview
YouTube Summarizer is a web application that extracts subtitles from YouTube videos and generates concise summaries using OpenAI's `llama-3.2-11b-vision-preview` model. The application is built with Streamlit for the frontend and a backend script to process transcripts and generate summaries.

## Features
- Extracts subtitles from YouTube videos
- Uses `llama-3.2-11b-vision-preview` to generate concise summaries
- Simple and interactive UI built with Streamlit
- Easy to install and use

## Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python
- **AI Model:** `llama-3.2-11b-vision-preview`
- **Libraries:** `streamlit`,`youtube_transcript_api`,`langchain`,`langchain_core`,`langchain-groq`

## Installation
### Prerequisites
Ensure you have Python installed (>= 3.8). Install required dependencies using:

```bash
pip install -r requirements.txt
```

### Clone the Repository
```bash
git clone https://github.com/your-username/youtube-summarizer.git
```

## Usage
### Running the Application
1. Start the Streamlit frontend:
   ```bash
   streamlit run MainFun.py
   ```
2. The application will open in your browser.
3. Enter a YouTube video URL and click the summarize button.

## Project Structure
```
📂 youtube-summarizer
├── 📄 MainFun.py       # Streamlit frontend
├── 📄 YoutubeSummery.py # Get Transcript
├── 📄 lama.py      # Backend script for transcript processing
├── 📄 requirements.txt            # Dependencies
├── 📄 README.md                   # Documentation
```

## Contributing
Contributions are welcome! Feel free to submit issues and pull requests.

## License
This project is licensed under the MIT License.

## Contact
For any questions, reach out at [kowsiganmv@gmail.com](kowsiganmv@gmail.com).

