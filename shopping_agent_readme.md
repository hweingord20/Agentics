<h1 align="center">Agentics</h1>
<p align="center">
    <img src="https://raw.githubusercontent.com/IBM/Agentics/refs/heads/main/image.png" height="128">
    <img src="https://raw.githubusercontent.com/IBM/Agentics/refs/heads/main/image.png" height="128">
</p>


- **Author:**
    - *Hailey Weingord*, Columbia MSDS, hnw2108@columbia.edu



# 🛍️ Shopping Agent with CrewAI + SerpApi Google Shopping

This project implements a **shopping research agent** using [CrewAI](https://docs.crewai.com/) and the **SerpApi Google Shopping tool**.  
The agent searches for products on Google Shopping, retrieves details like **title, price, merchant, and link**, and summarizes the best options.

---

## 🚀 Features
- Uses **CrewAI agents** to structure the shopping workflow.
- Integrates with **SerpApi** to fetch live Google Shopping results.
- Accepts any product query (e.g., *"fall knee-high boots"*, *"wireless noise-cancelling headphones"*).
- Produces structured, readable results.

---

## 📦 Requirements
- Python 3.12+
- [CrewAI](https://docs.crewai.com/)
- [crew-ai-tools](https://pypi.org/project/crewai-tools/)
- [PyYAML](https://pyyaml.org/)
- A **SerpApi API key**

## Command to Run Agent
python examples/crew_ai_shopping_agent.py

Install dependencies:

```bash
pip install crewai crewai-tools pyyaml