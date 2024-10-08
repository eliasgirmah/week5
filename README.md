# Named Entity Recognition (NER) for Amharic Text Using Transformers

This project focuses on fine-tuning various Transformer models (mBERT, XLM-Roberta, DistilBERT) for Named Entity Recognition (NER) on Amharic text. The models were evaluated using key performance metrics such as Precision, Recall, and F1-Score. The project also includes visualizations and model interpretability using SHAP or LIME to explain entity recognition predictions.

## Table of Contents

- [Project Overview](#project-overview)
- [Models](#models)
- [Installation](#installation)
- [Fine-Tuning and Evaluation](#fine-tuning-and-evaluation)


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
## Fine-Tuning and Evaluation

### Fine-Tuning Process

The models were fine-tuned using the Hugging Face `Trainer` API. Below is an example for fine-tuning the **XLM-Roberta** model:

```python
from transformers import XLMRobertaForTokenClassification, Trainer, TrainingArguments

model = XLMRobertaForTokenClassification.from_pretrained('xlm-roberta-base', num_labels=num_labels)

trainer = Trainer(
    model=model,
    args=TrainingArguments(
        output_dir='./results',
        num_train_epochs=2,
        per_device_train_batch_size=16
    ),
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    compute_metrics=compute_metrics
)

trainer.train()
### Evaluation Metrics

The following table summarizes the evaluation results for the fine-tuned models:

| Model        | Loss   | Precision | Recall | F1-Score |
|--------------|--------|-----------|--------|----------|
| mBERT        | 0.0028 | 99.97%    | 99.97% | 99.97%   |
| XLM-Roberta  | 0.0067 | 99.92%    | 99.92% | 99.92%   |
| DistilBERT   | 0.0069 | 99.92%    | 99.92% | 99.92%   |
