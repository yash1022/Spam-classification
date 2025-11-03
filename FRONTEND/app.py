import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download required NLTK data
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

ps = PorterStemmer()

def transform_text(text):
    """
    Preprocess the input text by:
    1. Converting to lowercase
    2. Tokenizing
    3. Removing special characters
    4. Removing stop words and punctuation
    5. Applying stemming
    """
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    # Remove special characters
    arr = []
    for i in text:
        if i.isalnum():
            arr.append(i)
    
    text = arr[:]
    arr.clear()
    
    # Remove stop words and punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            arr.append(i)
    
    text = arr[:]
    arr.clear()
    
    # Apply stemming
    for i in text:
        arr.append(ps.stem(i))
    
    return " ".join(arr)

# Load the pre-trained model and vectorizer
@st.cache_resource
def load_model():
    """Load the saved model and vectorizer"""
    try:
        tfidf = pickle.load(open('../MODELS/vectorizer.pkl', 'rb'))
        model = pickle.load(open('../MODELS/model.pkl', 'rb'))
        return tfidf, model
    except FileNotFoundError:
        st.error("Model files not found! Please ensure 'model.pkl' and 'vectorizer.pkl' exist in the MODELS folder.")
        return None, None

# Page configuration
st.set_page_config(
    page_title="SMS Spam Classifier",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        padding: 0.75rem;
        border-radius: 10px;
        border: none;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #FF6B6B;
    }
    .spam-result {
        background-color: #FFE5E5;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF4B4B;
    }
    .ham-result {
        background-color: #E5F5E5;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4BB543;
    }
    .header {
        text-align: center;
        padding: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='header'>", unsafe_allow_html=True)
st.title("📧 SMS Spam Classifier")
st.markdown("### Detect spam messages using Machine Learning")
st.markdown("</div>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    This application uses a **Multinomial Naive Bayes** classifier 
    trained on SMS data to detect spam messages.
    
    **Features:**
    - Text preprocessing (lowercase, tokenization)
    - Stop words removal
    - Stemming
    - TF-IDF vectorization
    
    **Accuracy:** ~97%
    """)
    
    st.header("📊 Model Info")
    st.write("""
    - **Algorithm:** Multinomial Naive Bayes
    - **Vectorizer:** TF-IDF
    - **Dataset:** SMS Spam Collection
    """)
    
    st.header("🎯 How to Use")
    st.write("""
    1. Enter or paste your SMS message
    2. Click on 'Predict'
    3. Get instant spam/ham classification
    """)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Enter Message")
    input_sms = st.text_area(
        "Type or paste your message here:",
        height=150,
        placeholder="e.g., Congratulations! You've won a $1000 gift card. Click here to claim now!",
        label_visibility="collapsed"
    )
    
    predict_button = st.button("🔍 Predict", use_container_width=True)

with col2:
    st.subheader("Quick Examples")
    
    spam_example = "WINNER!! As a valued customer, you have been selected to receive a £900 prize reward! Call now!"
    ham_example = "Hey, are we still meeting for lunch tomorrow at 12pm?"
    
    if st.button("Try Spam Example", use_container_width=True):
        input_sms = spam_example
        st.rerun()
    
    if st.button("Try Ham Example", use_container_width=True):
        input_sms = ham_example
        st.rerun()

# Prediction logic
if predict_button:
    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message to classify!")
    else:
        # Load model
        tfidf, model = load_model()
        
        if tfidf is not None and model is not None:
            with st.spinner("Analyzing message..."):
                # Preprocess
                transformed_sms = transform_text(input_sms)
                
                # Vectorize
                vector_input = tfidf.transform([transformed_sms])
                
                # Predict
                result = model.predict(vector_input)[0]
                
                # Get prediction probability
                proba = model.predict_proba(vector_input)[0]
                confidence = max(proba) * 100
            
            # Display result
            st.markdown("---")
            st.subheader("📊 Prediction Result")
            
            if result == 1:
                st.markdown(f"""
                <div class='spam-result'>
                    <h2 style='color: #FF4B4B; margin: 0;'>🚨 SPAM</h2>
                    <p style='margin: 10px 0 0 0; font-size: 18px;'>
                        Confidence: <strong>{confidence:.2f}%</strong>
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                st.warning("⚠️ This message appears to be spam. Be cautious!")
                
            else:
                st.markdown(f"""
                <div class='ham-result'>
                    <h2 style='color: #4BB543; margin: 0;'>✅ NOT SPAM (HAM)</h2>
                    <p style='margin: 10px 0 0 0; font-size: 18px;'>
                        Confidence: <strong>{confidence:.2f}%</strong>
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                st.success("✅ This message appears to be legitimate!")
            
            # Show processed text in an expander
            with st.expander("🔍 View Preprocessed Text"):
                st.code(transformed_sms, language=None)
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("Original Length", len(input_sms))
                with col_b:
                    st.metric("Processed Length", len(transformed_sms))

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>Built with ❤️ using Streamlit | Powered by Machine Learning</p>
</div>
""", unsafe_allow_html=True)
