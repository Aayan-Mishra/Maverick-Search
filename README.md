# Maverick-Search 🔍

## 1. Introduction
Maverick Search is an open-source AI search engine designed to run locally. Any local model can be used but Maverick models are optimised with this code. Maverick Search uses Exa Search API which more information can be found at [exa.ai](https://exa.ai/). This project is designed to be an open-source alternative to major AI search engines such as Perplexity and etc. While this project is not as accurate or as extensive as certain features whch can be found from other AI providers e.g Perplexity AI's Deep Research, this project aims to replicate that and allow users to run it locally without having to worry about data privacy. Maverick Search can also use other API models from OpenRouter for users that lack the compute to run the Maverick models locally.

## 2. Core Features

| **Feature**                    | **Description**                                                                 | **Benefits**                                                                 |
|---------------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **API-Based Search**            | Search is conducted through an API, allowing queries to be processed externally. | Simplifies setup and ensures flexibility in accessing search models remotely. |
| **Exa Search API Integration**  | Integrates with Exa Search API for enhanced search capabilities.                 | Users can access a wide range of powerful search models and results without heavy local compute. |
| **Maverick-Optimized Models**   | Exposes optimized Maverick models via the API for search queries.               | Delivers more tailored and accurate results through specialized AI models.   |
| **Privacy-Focused**             | The ability to run models locally ensures that users' data is not tracked or used to train models  | Ensures that user data remains secure and only temporarily used for searches. |
| **Customizable Search Options** | Users can configure search parameters and model settings through the API.       | Enables personalized search experiences based on user needs and preferences. |
| **Model Compatibility**         | Allows integration with other external models via the API for flexible search.  | Users can choose to use different AI models for their search tasks, offering more versatility. |

<p align="center">
  <img src="https://exa.imgix.net/simpleqa-eval-7.png?fm=avif&q=50" alt="Image" width=600 />
</p>

<p align="center">
  <em>Exa Search API compared to other search engines. Source: Exa AI</em>
</p>

## 3. Usage

This repository consists of 3 code files: **Engine, CLI and UI**

- **Engine:** This code file consists of just the Exa Search API call so that if you would like, you could build your own applications on the Exa python library. This is what Maverick-Search CLI and UI are based on
- **CLI:** This is the full code which consists of every feature e.g Search, Local Model usage and API model usage and etc. This is for more experienced users who want to use/modify the full code.
- **UI:** is a variation of CLI but has a Streamlit powered UI (Coming Soon)
