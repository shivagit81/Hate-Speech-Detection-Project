# Hate Speech Detection Project

## Overview

This project focuses on the development of a hate speech detection model using natural language processing (NLP) techniques and machine learning. The goal is to identify and classify hate speech in textual data, contributing to the ongoing efforts to address online toxicity and promote a safer online environment.

## Table of Contents

- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Dataset

The dataset used for this project is sourced from 'HateSpeechDatasetBalanced.csv,' containing labeled examples of text data with corresponding hate speech labels. The distribution of labels is analyzed during data exploration to understand the dataset's characteristics.
Link for dataset https://www.kaggle.com/datasets/waalbannyantudre/hate-speech-detection-curated-dataset
## Project Structure

The project is organized as follows:

- **`data/`**: Contains the dataset used for training and testing.
- **`notebooks/`**: Jupyter Notebooks used for data analysis, preprocessing, and model development.
- **`src/`**: Python source code for text preprocessing, model training, and evaluation.
- **`requirements.txt`**: Specifies the required Python packages for the project.
- **`README.md`**: Project documentation providing an overview, setup instructions, and usage guidelines.

## Setup

To set up the project locally, follow these steps:

1. Clone the repository
2. Navigate to the project directory
3. Create a virtual environment (optional but recommended): `python -m venv venv`
4. Activate the virtual environment: 
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Explore the Jupyter Notebooks in the `notebooks/` directory for data analysis and preprocessing insights.
2. Run the Python scripts in the `src/` directory for model training and evaluation.
3. Adjust parameters and configurations based on specific requirements.

## Technologies Used

- Python
- Pandas
- NLTK (Natural Language Toolkit)
- Scikit-learn
- Jupyter Notebooks
- Matplotlib
- Seaborn
- Git

## Contributing

If you would like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
