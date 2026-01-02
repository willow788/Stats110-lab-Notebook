<div align="center">

# 🎲 Stats 110 Lab Notebook

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Statistics](https://img.shields.io/badge/Statistics-FF6B6B?style=for-the-badge&logo=chartdotjs&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)

<h3>✨ A computational journey through Harvard's Stats 110 ✨</h3>

*Transforming theoretical probability concepts into beautiful Python implementations*

[![License:MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=willow788.Stats110-lab-Notebook)
![Last Commit](https://img.shields.io/github/last-commit/willow788/Stats110-lab-Notebook?style=flat-square)

[📚 Concepts](#-concepts-implemented) • [🚀 Quick Start](#-quick-start) • [📂 Structure](#-repository-structure) • [🎯 Philosophy](#-learning-philosophy)

</div>

---

## 💡 About This Project

> **"The only way to learn mathematics is to do mathematics."** — Paul Halmos

Welcome to my **Stats 110 Lab Notebook**! This repository is my personal computational laboratory where I bridge the gap between statistical theory from Harvard's legendary Stats 110 course and hands-on Python implementations. 

### 🌟 Why This Exists

While I'm currently studying Gaussian distributions in Stats 110, I realized that truly understanding probability requires **doing** probability.  This notebook is my journey from scratch — implementing every concept, visualizing every distribution, and coding every theorem I encounter. 

<div align="center">

```
┌─────────────────────────────────────────┐
│  📖 Learn Theory → 💭 Understand Math   │
│         ↓                               │
│  💻 Code It → 🎨 Visualize It           │
│         ↓                               │
│  🧪 Experiment → 📝 Document Insights   │
└─────────────────────────────────────────┘
```

</div>

---

## 🎯 Project Goals

<table>
<tr>
<td width="50%">

### 📚 **Learn by Doing**
- Implement every Stats 110 concept in Python
- Build intuition through visualization
- Connect theory with practice

</td>
<td width="50%">

### 🔬 **Experiment & Explore**
- Test edge cases and special scenarios
- Create beautiful visualizations
- Document insights and "aha!" moments

</td>
</tr>
</table>

---

## 📖 Concepts Implemented

### ✅ **Current Implementations**

<table>
<tr>
<td width="50%">

#### 🎲 **Sample Space Foundations**
**Location:** `What is Sample space?/`

- **`pebble.py`** - Advanced "pebble world" visualization
  - Interactive sample space representations
  - Customizable color palettes & themes
  - Dynamic probability scaling
  - Beautiful sparkle effects ✨
  
**Features:**
- Visual representation of probability spaces
- Intuitive outcome probability mapping
- Highly customizable aesthetics

</td>
<td width="50%">

#### 📊 **Naive Probability**
**Location:** `Naive definition of Probability/`

- **`naive.py`** - Classical probability implementation
  - `NaiveSampleSpace` class
  - Event probability calculations
  - Support for discrete outcomes
  
**Examples Included:**
- 🪙 Coin flips
- 🎲 Dice rolls  
- Generic finite sample spaces

</td>
</tr>
</table>

### 🚧 **Coming Soon**

<details>
<summary><b>🔮 Click to see the roadmap</b></summary>

As I progress through Stats 110, I'll be implementing: 

- 🎯 **Probability Axioms** - Formal probability foundations
- 🔢 **Counting Principles** - Permutations, combinations, binomial coefficients
- 🎪 **Conditional Probability** - Bayes' theorem and applications
- 📊 **Discrete Random Variables** - PMFs, expectation, variance
- 📈 **Common Distributions** - Binomial, Poisson, Geometric, Negative Binomial
- 🌊 **Continuous Random Variables** - PDFs, CDFs, transformations
- 🔔 **Gaussian/Normal Distribution** - The bell curve and its properties
- 🎰 **Joint Distributions** - Multivariate probability, independence
- 🔗 **Covariance & Correlation** - Relationships between random variables
- 📉 **Limit Theorems** - Law of Large Numbers, Central Limit Theorem
- 🧮 **Moment Generating Functions** - MGFs and their applications
- 🎲 **Markov Chains** - Stochastic processes (if we get there!)

*This list grows as my Stats 110 journey continues!*

</details>

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.7+ recommended
python --version

# Required packages
pip install matplotlib seaborn numpy
```

### Installation

```bash
# Clone the repository
git clone https://github.com/willow788/Stats110-lab-Notebook.git

# Navigate to directory
cd Stats110-lab-Notebook
```

### 🎨 Try It Out! 

#### Example 1: Naive Probability (Coin Flip)
```python
from Naive_definition_of_Probability. naive import NaiveSampleSpace

# Create a fair coin
coin = NaiveSampleSpace(['H', 'T'])

# Calculate probabilities
print(f"P(Heads) = {coin.probability(['H'])}")  # Output: 0.5
print(f"P(Tails) = {coin.probability(['T'])}")  # Output: 0.5
```

#### Example 2: Pebble World Visualization
```python
from What_is_Sample_space. pebble import SampleSpace

# Create a loaded die
loaded_die = SampleSpace({
    1: 0.1,
    2: 0.1,
    3: 0.1,
    4: 0.1,
    5: 0.1,
    6: 0.5  # Loaded towards 6! 
})

# Visualize the probability space
loaded_die.visualize(
    title="🎲 Loaded Die - Pebble World",
    show_sparkles=True
)
```

---

## 📂 Repository Structure

```
Stats110-lab-Notebook/
│
├── 📁 What is Sample space?/
│   ├── pebble.py                    # Advanced visualization class
│   └── message+credits.txt          # Development notes
│
├── 📁 Naive definition of Probability/
│   └── naive.py                     # Classical probability implementation
│
├── 📄 README.md                     # You are here!  👋
├── 📄 LICENSE                       # MIT License
└── 📄 .gitignore                    # Git configuration
```

---
### 🧠 Core Principles

- 🎯 **Active Learning** - No passive consumption; every concept gets coded
- 🎨 **Visual Thinking** - Beautiful visualizations reveal deep insights  
- 🔬 **Experimentation** - Playing with code builds intuition
- 📝 **Documentation** - Writing about concepts reinforces learning
- 🚀 **Iteration** - Starting from scratch, building progressively

---

## 🛠️ Technologies & Tools

<div align="center">

| Tool | Purpose |
|------|---------|
| ![Python](https://img.shields.io/badge/Python_3.x-3776AB?style=flat-square&logo=python&logoColor=white) | Core programming language |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square) | Primary visualization library |
| ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat-square) | Statistical visualization |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) | Numerical computing (when needed) |
| ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white) | Interactive experimentation (future) |

</div>

---

## 📈 Progress Tracker

<div align="center">

### 🎯 Stats 110 Concept Coverage

```
Foundation Concepts:      [██████░░░░░░░░░░░░░░] 30%
Discrete Distributions:  [██░░░░░░░░░░░░░░░░░░]  5%
Continuous Distributions:[░░░░░░░░░░░░░░░░░░░░]  0%
Advanced Topics:         [░░░░░░░░░░░░░░░░░░░░]  0%
```

**Overall Progress:** `~10%` Complete

*Last updated: January 2026*

</div>

---

## 🤝 Contributing

While this is primarily a personal learning project, I absolutely welcome: 

- 🐛 **Bug reports** - If something doesn't work as expected
- 💡 **Suggestions** - Better algorithms, cleaner code, or optimization ideas
- 🎨 **Visualization ideas** - New ways to visualize probability concepts  
- 📚 **Additional examples** - Interesting edge cases or applications
- 🌟 **Encouragement** - Learning in public is vulnerable; kind words appreciated! 

Feel free to [open an issue](https://github.com/willow788/Stats110-lab-Notebook/issues) or submit a pull request!

---

## 📚 Resources & Inspiration

- 🎓 [**Harvard Stats 110**](https://projects.iq.harvard.edu/stat110) - The legendary probability course by Prof. Joe Blitzstein
- 📖 [**Introduction to Probability (Blitzstein & Hwang)**](http://probabilitybook.net/) - The companion textbook
- 🐍 [**Python Documentation**](https://docs.python.org/3/) - For implementation reference
- 🎨 [**Matplotlib Gallery**](https://matplotlib.org/stable/gallery/index.html) - Visualization inspiration

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

Feel free to use, modify, and learn from this code! 

---

## 🙏 Acknowledgments

- **Prof. Joe Blitzstein** - For making Stats 110 freely available and genuinely inspiring
- **Harvard Statistics Department** - For world-class educational resources
- **Python Community** - For incredible libraries that make visualization beautiful
- **GitHub Copilot** - For helping make `pebble.py` visually stunning (credits where it's due!)
- **You** - For being interested in this learning journey!  🌟

---

<div align="center">

### 💭 *"Statistics is the grammar of science."* — Karl Pearson

### 💫 **Happy Learning!  May your p-values be significant and your distributions be normal!** 📊🐍

---

<sub>Built with 💙, ☕, and lots of probability by <a href="https://github.com/willow788">@willow788</a></sub>

<sub>⭐ Star this repo if you find it helpful! It motivates me to keep learning and documenting!  ⭐</sub>

</div>
