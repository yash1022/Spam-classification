# SMS Spam Classifier - Streamlit App

A beautiful and interactive web application for detecting spam SMS messages using Machine Learning.

## Features

- 🎯 **Real-time Spam Detection**: Classify SMS messages as spam or ham instantly
- 📊 **Confidence Score**: See the model's confidence in its prediction
- 🔍 **Text Preprocessing Visualization**: View how your message is processed
- 💡 **Quick Examples**: Test with pre-loaded spam and ham examples
- 🎨 **Modern UI**: Clean and intuitive user interface

## Tech Stack

- **Frontend**: Streamlit
- **ML Model**: Multinomial Naive Bayes
- **Vectorization**: TF-IDF
- **NLP**: NLTK (tokenization, stemming, stopwords removal)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Navigate to the FRONTEND directory:
```bash
cd FRONTEND
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Download NLTK data (if not already downloaded):
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

## Running the Application

1. Make sure you're in the FRONTEND directory
2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. The app will open in your default browser at `http://localhost:8501`

## Usage

1. **Enter a Message**: Type or paste an SMS message in the text area
2. **Click Predict**: Press the "🔍 Predict" button to classify the message
3. **View Results**: See if the message is spam or ham with confidence score
4. **Try Examples**: Use the quick example buttons to test the classifier

## Model Information

- **Algorithm**: Multinomial Naive Bayes
- **Accuracy**: ~97%
- **Features**: TF-IDF vectorized text features
- **Training Data**: SMS Spam Collection Dataset

## Preprocessing Pipeline

The application performs the following preprocessing steps:

1. **Lowercase Conversion**: Converts all text to lowercase
2. **Tokenization**: Splits text into individual words
3. **Special Character Removal**: Removes non-alphanumeric characters
4. **Stop Words Removal**: Removes common English stop words
5. **Stemming**: Reduces words to their root form using Porter Stemmer

## Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Select the FRONTEND/app.py file
5. Deploy!

### Deploy to Heroku

1. Create a `Procfile`:
```
web: sh setup.sh && streamlit run app.py
```

2. Create a `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
```

3. Deploy using Heroku CLI

## Project Structure

```
FRONTEND/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file

MODELS/
├── model.pkl          # Trained ML model
└── vectorizer.pkl     # TF-IDF vectorizer
```

## Screenshots

### Main Interface
The clean and intuitive interface allows users to easily input messages and get instant predictions.

### Spam Detection
Messages classified as spam are highlighted in red with a warning indicator.

### Ham Detection
Legitimate messages are highlighted in green with a success indicator.

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available under the MIT License.

## Contact

For questions or feedback, please open an issue on GitHub.

---

Built with ❤️ using Streamlit and Machine Learning
