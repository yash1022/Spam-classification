# 🚀 Quick Start Guide

This guide will help you get the SMS Spam Classifier up and running in minutes!

## Option 1: Run with Batch File (Windows - Easiest)

1. Navigate to the `FRONTEND` folder
2. Double-click `run_app.bat`
3. Your browser will open automatically at `http://localhost:8501`

## Option 2: Run with Command Line

### Windows (PowerShell)
```powershell
cd FRONTEND
streamlit run app.py
```

### Mac/Linux
```bash
cd FRONTEND
streamlit run app.py
```

## First Time Setup

If you haven't installed the dependencies yet:

```bash
pip install -r FRONTEND/requirements.txt
```

This will install:
- streamlit
- nltk
- scikit-learn
- pandas
- numpy

## Troubleshooting

### NLTK Data Missing
If you see errors about missing NLTK data, run:
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

### Model Files Missing
Make sure `model.pkl` and `vectorizer.pkl` exist in the `MODELS` folder.
If not, run the `MODEL_TRAINING.ipynb` notebook to generate them.

### Port Already in Use
If port 8501 is busy, run:
```bash
streamlit run app.py --server.port 8502
```

## Testing the Application

Once the app is running:

1. **Try the Examples**: Click "Try Spam Example" or "Try Ham Example"
2. **Enter Your Own Text**: Type any message in the text area
3. **View Results**: See the classification, confidence score, and preprocessed text

## Sample Messages to Test

### Spam Examples:
- "WINNER!! You've been selected to receive a $1000 gift card. Click here now!"
- "Congratulations! You have won a free iPhone. Call 123-456-7890 to claim."
- "URGENT! Your account will be suspended. Verify now at fake-link.com"

### Ham Examples:
- "Hey, are we still meeting for lunch tomorrow?"
- "Can you pick up milk on your way home?"
- "Thanks for the help yesterday! Really appreciated it."

## Next Steps

- Read the full [README.md](../README.md) for project details
- Check [FRONTEND/README.md](README.md) for deployment options
- Explore the notebooks in `NOTEBOOK/` folder to understand the ML pipeline

## Need Help?

- Check the [Issues](https://github.com/yash1022/Spam-classification/issues) page
- Read the documentation in README files
- Contact the project maintainer

---

Happy Spam Detecting! 🎯
