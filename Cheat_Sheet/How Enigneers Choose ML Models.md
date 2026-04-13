# How Enigneers Choose ML Models



### Step-1 Problem Framing:

what type of problem?

* regression
* classification
* ranking
* clustering
* forecasting
* anomaly detection

**Wrong Framing -> Wrong model**



### Step-2 Understand Data

Data dictates model choice

Check:

* Structured vs unstructures
* Dataset size
* Noise \& Missing Values
* Feature Quality
* Class Imbalance

**Model Fail when data is Ignored**



### Step-3 Constraints First

Real systems have limits

Consider:

* Latency requirements
* Compute budget
* memory footprint
* Interpretability needs
* Training time

**Engineering != Kaggle**



### Step-4 Establish Baselines

Before complexity

Try:

* Linear/ Logistic Regression
* Tree-based Models
* simple Heuristics

**No Baseline -> No Reference**



### Step-5 Error Analysis

Models don't just "improve"

Inspect:

* Failure Cases
* Bias vs Variance
* Data Leakage
* Feature issue

**Debugging >>> Guessing**



### Step-6 Increase Complexity (if needed)

Only when justified

Ask:

* Is baseline insufficient?
* is data volume adequate?
* Do gains justify cost?

**Complexity is Expensive**



#### Best Models != most complex

##### Best Model =

* Fits problem
* Fits Data
* Fits constraints
* Stable in production

