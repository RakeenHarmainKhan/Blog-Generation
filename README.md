# 🌐 AI Blog Generator with LLaMA 2 & Streamlit

Welcome to the **AI Blog Generator**, a sleek and simple web app that helps you generate professional blogs with just a topic and a click! Whether you're a **data scientist**, **researcher**, or just someone curious, this app creates custom-tailored blog content using the **LLaMA 2 language model**.

> ⚡ Powered by LangChain + LLaMA 2 + Streamlit

---

## 📸 Preview

| Input View | Output View |
|------------|-------------|
| ![Screenshot 2025-06-22 121546](https://github.com/user-attachments/assets/de9b9769-f031-4da9-8d05-088e2dea5c88)
 | ![Screenshot 2025-06-22 121754](https://github.com/user-attachments/assets/c9982a45-9af8-4852-94d6-7b66205fc60d)
 |

---

## ✨ Features

- 📝 Enter any **blog topic** you want
- 🎯 Choose your **audience style** (Researchers, Data Scientists, Common People)
- 🔢 Specify the **desired word count**
- 🤖 LLaMA 2 handles the generation using a local `.bin` model
- 📃 Outputs a clean, readable blog post
- 🌗 Supports **dark mode** and has a visually refined interface

---

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io/)** – frontend interface  
- **[LangChain](https://www.langchain.com/)** – prompt management  
- **[CTransformers](https://github.com/marella/ctransformers)** – for running the model locally  
- **Meta's LLaMA 2** – LLaMA 2 7B Chat model (quantized `.ggmlv3.q8_0` version)

---

## 📦 LLaMA 2 Model Used

We used the **LLaMA 2 7B Chat** model: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin

