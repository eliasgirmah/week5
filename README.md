# Named Entity Recognition (NER) for Amharic Text Using Transformers

This project focuses on fine-tuning various Transformer models (mBERT, XLM-Roberta, DistilBERT) for Named Entity Recognition (NER) on Amharic text. The models were evaluated using key performance metrics such as Precision, Recall, and F1-Score. The project also includes visualizations and model interpretability using SHAP or LIME to explain entity recognition predictions.

## Table of Contents

- [Project Overview](#project-overview)
- [Models](#models)
- [Installation](#installation)
- [Fine-Tuning and Evaluation](#fine-tuning-and-evaluation)
- [Model Interpretability](#model-interpretability)
- [Visualizations](#visualizations)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

The goal of this project is to build a robust NER system for Amharic text using pre-trained Transformer models. The fine-tuning process leverages models like mBERT and XLM-Roberta to recognize entities such as products, prices, and locations in Amharic text. The key components include:

- **Fine-tuning**: Training pre-trained models on labeled NER data.
- **Evaluation**: Using metrics such as Precision, Recall, and F1-Score.
- **Model Interpretability**: Implementing SHAP or LIME for understanding how models identify entities.
- **Visualization**: Tokenization, Confusion Matrix, and Entity Distribution visualizations.

---

## Models

The following models were fine-tuned and evaluated:

- **mBERT** (Multilingual BERT)
- **XLM-Roberta**
- **DistilBERT** (Distilled version of BERT)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/eliasgirmah/week5.git
   cd week5
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
