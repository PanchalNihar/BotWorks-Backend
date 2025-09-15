# Solar Power Prediction Model

A machine learning project that predicts solar power generation using weather data and historical patterns.

## 📊 Project Overview

This project implements a machine learning model to predict solar power generation based on various environmental factors. The system combines weather data APIs with trained models to provide accurate solar power forecasts.

## 🚀 Features

- **Machine Learning Model**: Trained model for solar power prediction using historical data
- **Model Persistence**: Saved model checkpoints for quick loading and inference
- **Angular Frontend**: Interactive web interface with animations and scatter plots

## 📁 Project Structure

```
solar-prediction/
├── .ipynb_checkpoints/          # Jupyter notebook checkpoints
├── .env                         # Environment variables
├── .gitignore                   # Git ignore file
├── app.py                       # Main Flask/FastAPI application
├── requirements.txt             # Python dependencies
├── solar_final.ipynb           # Final analysis notebook
├── solar_model_train.ipynb     # Model training notebook
├── solar_power_model.pkl       # Trained model file
├── spg.csv                     # Solar power generation dataset
├── updated_power_generation_data.csv  # Updated dataset
└── README.md                   # Project documentation
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Node.js (for Angular frontend)
- pip (Python package manager)

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd solar-prediction
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

## 📊 Model Training

The project includes comprehensive Jupyter notebooks for model development:

### Training Process
1. **Data Collection**: Historical solar power generation data
2. **Data Preprocessing**: Cleaning, feature engineering, and normalization
3. **Model Selection**: Comparison of different ML algorithms
4. **Training**: Model training with cross-validation
5. **Evaluation**: Performance metrics and validation
6. **Model Persistence**: Saving trained model as `.pkl` file

### Key Notebooks
- `solar_model_train.ipynb`: Complete model training pipeline
- `solar_final.ipynb`: Final analysis and model evaluation

## 🌐 API Endpoints

### Prediction Endpoints
```
POST /predict
Content-Type: application/json

{
  "temperature": 25.5,
  "humidity": 60,
  "solar_irradiance": 800,
  "wind_speed": 3.2
}
```

### Weather Integration
```
GET /weather/current
GET /weather/forecast
```

## 🎨 Frontend Integration

The project includes an Angular frontend with:
- **Interactive Dashboard**: Real-time predictions and visualizations
- **Scatter Plot Visualizations**: Data analysis charts
- **Animations**: Smooth UI transitions
- **Responsive Design**: Mobile-friendly interface


## 🔧 Configuration

### Environment Variables
```
WEATHER_API_KEY=your_weather_api_key


## 📊 Data Sources

- **Historical Solar Data**: Solar power generation records
- **Weather APIs**: Real-time weather information
- **Solar Irradiance Data**: Solar radiation measurements

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Weather data providers
- Solar energy datasets
- Machine learning libraries and frameworks

---

⭐ **Star this repository if you find it helpful!**
