# 📧 SMS Spam Classification System

A complete end-to-end machine learning project for detecting spam SMS messages using Natural Language Processing and Naive Bayes classification.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-red.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 Project Overview

This project implements a machine learning-based spam classifier that can accurately detect spam messages in SMS text. It includes:

- 📊 **Exploratory Data Analysis (EDA)**
- 🔧 **Data Preprocessing Pipeline**
- 🤖 **Multiple ML Models Training**
- 🌐 **Interactive Web Application**
- 📦 **Ready for Deployment**

## ✨ Features

- **High Accuracy**: Achieves ~97% accuracy using Multinomial Naive Bayes
- **Real-time Predictions**: Instant spam detection through web interface
- **Text Preprocessing**: Complete NLP pipeline (tokenization, stemming, stop words removal)
- **Model Comparison**: Evaluated multiple Naive Bayes variants (Gaussian, Multinomial, Bernoulli)
- **Beautiful UI**: Modern and intuitive Streamlit interface
- **Deployment Ready**: Configured for Streamlit Cloud, Heroku, and other platforms

## 📁 Project Structure

```
Spam-classification/
│
├── DATASET/                    # Dataset files
│   ├── spam.csv               # Original dataset
│   ├── cleaned_data.csv       # Cleaned dataset
│   └── final_data.csv         # Preprocessed dataset
│
├── NOTEBOOK/                   # Jupyter notebooks
│   ├── EDA.ipynb              # Exploratory Data Analysis
│   ├── PREPROCESSING.ipynb    # Data preprocessing
│   └── MODEL_TRAINING.ipynb   # Model training and evaluation
│
├── MODELS/                     # Saved models
│   ├── model.pkl              # Trained ML model (Multinomial NB)
│   └── vectorizer.pkl         # TF-IDF vectorizer
│
├── FRONTEND/                   # Streamlit web application
│   ├── app.py                 # Main application file
│   ├── requirements.txt       # Python dependencies
│   ├── run_app.bat           # Windows launcher
│   ├── Procfile              # Heroku deployment
│   ├── setup.sh              # Deployment setup
│   ├── packages.txt          # System packages
│   └── README.md             # Frontend documentation
│
├── BACKEND/                    # Backend services (if any)
│
└── README.md                   # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yash1022/Spam-classification.git
cd Spam-classification
```

2. **Install dependencies**
```bash
pip install -r FRONTEND/requirements.txt
```

3. **Run the application**
```bash
cd FRONTEND
streamlit run app.py
```

Or simply double-click `run_app.bat` on Windows!

4. **Open your browser**
Navigate to `http://localhost:8501`

## 📊 Dataset

The project uses the **SMS Spam Collection Dataset** containing:
- 5,574 SMS messages
- Labeled as 'spam' or 'ham' (legitimate)
- Publicly available dataset for research

## 🔬 Machine Learning Pipeline

### 1. Data Preprocessing
- Lowercase conversion
- Tokenization using NLTK
- Special character removal
- Stop words removal
- Porter Stemming

### 2. Feature Extraction
- TF-IDF Vectorization
- Converts text to numerical features

### 3. Model Training
Trained and compared three Naive Bayes variants:
- **Gaussian Naive Bayes**
- **Multinomial Naive Bayes** ⭐ (Best performer)
- **Bernoulli Naive Bayes**

### 4. Model Evaluation
- Accuracy Score
- Precision Score
- Confusion Matrix
- Performance Visualization

## 📈 Results

| Model | Accuracy | Precision |
|-------|----------|-----------|
| Gaussian NB | ~88% | ~85% |
| **Multinomial NB** | **~97%** | **~100%** |
| Bernoulli NB | ~98% | ~99% |

**Selected Model**: Multinomial Naive Bayes for optimal balance of accuracy and precision.

## 🌐 Web Application

The Streamlit web application provides:
- Clean and intuitive user interface
- Real-time spam detection
- Confidence score display
- Text preprocessing visualization
- Quick example buttons for testing
- Responsive design

### Screenshots

*Coming soon*

## 🚢 Deployment

### Streamlit Cloud (Recommended)

1. Push code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect repository
4. Select `FRONTEND/app.py`
5. Deploy!

### Heroku

```bash
cd FRONTEND
heroku create your-app-name
git push heroku main
```

### Local Deployment

```bash
cd FRONTEND
streamlit run app.py --server.port 8501
```

## 🛠️ Technologies Used

- **Python 3.8+**
- **Streamlit** - Web framework
- **scikit-learn** - Machine learning
- **NLTK** - Natural language processing
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Matplotlib/Seaborn** - Data visualization
- **Pickle** - Model serialization

## 📝 Usage Examples

### Using the Web Interface

1. Enter or paste an SMS message
2. Click "Predict"
3. View the classification result (Spam/Ham)
4. See the confidence score
5. Check the preprocessed text

### Using the Model Programmatically

```python
import pickle
import nltk
from nltk.stem.porter import PorterStemmer

# Load model and vectorizer
model = pickle.load(open('MODELS/model.pkl', 'rb'))
vectorizer = pickle.load(open('MODELS/vectorizer.pkl', 'rb'))

# Preprocess text (use transform_text function)
# ... preprocessing code ...

# Predict
result = model.predict(vectorizer.transform([processed_text]))
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Yash**
- GitHub: [@yash1022](https://github.com/yash1022)

## 🙏 Acknowledgments

- SMS Spam Collection Dataset providers
- Streamlit team for the amazing framework
- scikit-learn and NLTK communities

## 📧 Contact

For questions or feedback, please open an issue on GitHub or contact through the repository.

---

⭐ If you found this project helpful, please consider giving it a star!

**Built with ❤️ using Python and Machine Learning**