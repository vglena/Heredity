# 🧬 Heredity AI: Gene and Trait Probability Calculator

This project calculates the probability distributions of genes and traits in a family using **Bayesian inference** and **probabilistic reasoning**.  
Given family data and known traits, the AI computes the probability that each person has 0, 1, or 2 copies of a gene, and whether they exhibit a particular trait.

---

## 📖 Overview

The program uses a dataset of family relationships and traits:

- Each CSV file in `data/` contains columns: `name`, `mother`, `father`, `trait`.  
- The trait column can be `1` (has trait), `0` (does not have trait), or empty (unknown).  
- Using **conditional probabilities**, **mutations**, and the **law of inheritance**, the AI calculates probabilities for each person.

The project focuses on computing:

1. **Joint probabilities** – Probability of a specific configuration of genes and traits across all family members.  
2. **Updates** – Adding new evidence to existing probability distributions.  
3. **Normalization** – Ensuring all probability distributions sum to 1 while maintaining relative proportions.

---

## ⚙️ How It Works

The project contains the following main file:

### `heredity.py`

- **joint_probability(people, one_gene, two_genes, have_trait)**  
  Computes the joint probability of a specific assignment of genes and traits for all people in the dataset.  
  - Accounts for inheritance from parents if available.  
  - Considers mutation probabilities.  
  - Uses conditional probabilities for traits based on gene counts.

- **update(probabilities, one_gene, two_genes, have_trait, p)**  
  Adds a new joint probability `p` to the existing probability distributions for each person.

- **normalize(probabilities)**  
  Normalizes all gene and trait distributions so that each sums to 1, preserving relative proportions.

---

## 🧩 File Structure

```text
heredity-ai/
│
├── heredity.py           # Core AI logic for calculating probabilities
├── data/                 # CSV files containing family data
│   ├── family0.csv
│   ├── family1.csv
│   └── ...
├── LICENSE               # MIT License
└── README.md             # Documentation (this file)
```
## ▶️ Usage
1. Clone the repository:
```python
git clone https://github.com/yourusername/heredity-ai.git
cd heredity-ai
```
2. Install dependencies:
```python
pip install -r requirements.txt
```
3. Run the AI:
```python
python heredity.py data/family0.csv
```
- Outputs the probability distribution for each person’s gene count and trait.

## 🧩 Dependencies / Requirements
- Python 3.8 or higher
- No third-party libraries required, though numpy or pandas can be used for additional analysis (optional)

Example `requirements.txt`:
```python
numpy>=1.21.0
pandas>=1.3.0
```
## 💡 Notes

- `PROBS` dictionary defines all relevant probabilities:
  - Gene distribution: Probability a person has 0, 1, or 2 copies of the gene without parental information.
  - Trait distribution: Probability a person exhibits a trait given their gene count.
  - Mutation probability: Chance a gene mutates when passed from parent to child.
- The AI calculates probabilities by:
  - Enumerating all possible gene/trait combinations.
  - Multiplying the relevant probabilities for each person.
  - Summing over combinations consistent with known evidence.
  - Normalizing the resulting distributions.

## 🏁 Credits

Inspired by CS50 AI’s Heredity Project for probabilistic reasoning and Bayesian networks.
Educational purpose: demonstrates inheritance modeling and conditional probability.

## 📄 License
```text
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
