<h1>Data Preprocessing Experiment</h1>
<h3>Overview</h3>
<p>This repository demonstrates my experimentation with preprocessing traffic data for my Google Summer of Code 2025 project,<br>
  "Smart Cities - Traffic Prediction Microservice." Using a Kaggle traffic dataset, I’ve applied techniques to handle missing values,<br> 
  cap outliers, and store data efficiently, ensuring it’s ready for machine learning models like LSTM.</p>

<h3>Purpose</h3>
<p>The goal is to showcase my ability to clean and structure large-scale traffic data, a critical step in building an effective traffic prediction system.<br> 
  This proof-of-work supports my GSoC proposal by preparing real-world data for deployment in a Kubernetes-based microservice.</p>

<h3>Dataset</h3>
<pre>Source: Kaggle "Traffic Prediction Dataset"
URL: <a href="https://www.kaggle.com/datasets/fedesoriano/traffic-prediction-dataset">Traffic Prediction Dataset</a>
File: traffic.csv </pre>

<h3>Columns Used:</h3>
<pre>date_time: Timestamp of traffic measurements.
vehicles: Hourly vehicle count.
Challenges: Missing values (e.g., sensor failures) and outliers (e.g., unrealistic spikes).</pre>
<pre>pip install pandas numpy pyarrow</pre>



![Screenshot 2025-04-07 203920](https://github.com/user-attachments/assets/2719fbb4-bf76-4032-ac51-f934a7674223)
