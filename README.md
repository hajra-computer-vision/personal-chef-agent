# 🍲 Personal Chef Agent — Heart-Healthy Edition

An LLM agent built with LangChain that suggests recipes based on the ingredients a user has on hand — customized for **heart patients**, with a calorie-awareness tool and image-based ingredient detection layered on top of the original course project.

---

## 🙏 Credit & Origin

This project is based on the **"Personal Chef"** project from LangChain Academy's official course, **[Introduction to LangChain - Python](https://academy.langchain.com/courses/foundation-introduction-to-langchain-python)**.

The original companion repository is:
🔗 **[langchain-ai/lca-lc-foundations](https://github.com/langchain-ai/lca-lc-foundations?tab=MIT-1-ov-file)** (MIT License)

If you want to build the base version of this project yourself, **start with the original repository above** — it has the full course setup, all three modules (Create Agent, Advanced Agent, Production-Ready Agent), and the original Personal Chef notebook this project extends. This repo assumes you're already familiar with that base and documents only what I changed and added on top of it.

---

## ✨ What's Different in This Version

This is not a copy of the course project — it's an extension built for a specific use case: **a personal chef agent designed for people managing heart health**, with two additions beyond the original tutorial:

### 1. Calorie Calculation Tool (new)
A custom tool was added that calculates approximate calorie counts for suggested recipes, so the agent can reason about calorie load — not just ingredients — when tailoring suggestions for a heart-healthy diet.

### 2. Heart-Patient-Focused Prompting
The agent's system prompt and recipe logic were adjusted to prioritize heart-healthy choices (e.g. lower sodium, lower saturated fat) rather than general-purpose recipe suggestions.

### 3. Image-Based Ingredient Detection (new)
If a user doesn't type out their available ingredients, they can instead **upload a photo of their fridge/pantry**, and the agent uses multimodal image analysis to identify ingredients directly from the image before suggesting a recipe.

---

## 🦙 Running with Ollama (Open-Source Models)

Unlike the original course (which primarily uses OpenAI's `gpt-5-nano`), **this project was tested using open-source models via Ollama**, so it can run locally without an API key or per-token cost.

### Setup Steps

**1. Install Ollama**
Download and install from [ollama.com](https://ollama.com) for your OS.

**2. Pull a model**
```bash
ollama pull llama3.1
```
*(Any tool-calling-capable Ollama model works — `llama3.1`, `qwen2.5`, or `mistral-nemo` are good choices. For image-based ingredient detection, use a vision-capable model such as `llava` or `llama3.2-vision`.)*

**3. Confirm Ollama is running**
```bash
ollama list
```
This should show your pulled model(s). Ollama runs a local server automatically after installation.

**4. Install the LangChain Ollama integration**
```bash
pip install langchain-ollama
```

**5. Use it in code**
```python
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.1",
    temperature=0.3,
)
```

For the image-analysis feature specifically, use a vision-capable model:
```python
vision_llm = ChatOllama(
    model="llama3.2-vision",
    temperature=0.2,
)
```

**6. No API key required**
Since Ollama runs models locally, no `OPENAI_API_KEY` or similar is needed for the core agent — only add a `TAVILY_API_KEY` in your `.env` if you're using the search tool from the original course.

---

## 🖼️ How Image-Based Ingredient Detection Works

If the user doesn't list ingredients in their prompt, they can instead attach a photo (e.g. of their fridge or pantry). The agent:
1. Passes the image to a vision-capable model (via `langchain_ollama`'s multimodal support, or an equivalent vision LLM)
2. Extracts a list of visible ingredients from the image
3. Feeds that ingredient list into the same recipe-suggestion + calorie-calculation flow used for typed input

This means the agent works whether the user types ingredients, uploads a photo, or does both.

---

## ▶️ How to Run

1. Clone this repo
2. Install Ollama and pull a model (see setup steps above)
3. `pip install -r requirements.txt`
4. If using the search tool, copy `example.env` to `.env` and add your `TAVILY_API_KEY`
5. Run the notebook or `python personal_chef.py`

## 📚 Base Course Reference

For the underlying concepts this project builds on (tool-calling, short-term memory, multimodal messages, agent design), see the original course modules in **[langchain-ai/lca-lc-foundations](https://github.com/langchain-ai/lca-lc-foundations?tab=MIT-1-ov-file)**:
- Module 1: Create Agent (foundational models, tools, memory, multimodal messages, Personal Chef project)
- Module 2: Advanced Agent (MCP, context/state, multi-agent systems)
- Module 3: Production-Ready Agent (middleware, HITL, dynamic agents)
