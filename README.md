# mindmate-hackvortex2025

# 🧠 MindMate – Mental Health Micro-Coach for Students

## 💡 Problem Statement

College students silently struggle with stress, anxiety, burnout, and academic pressure. Yet, most don’t seek therapy due to stigma, cost, or lack of access. There's a dire need for a private, intelligent, and supportive digital companion to help students manage their mental health daily.

## 🚀 Solution

**MindMate** is a web/mobile app that acts as a personal **micro-coach** for students, powered by AI. 
It enables:

- ✍️ Daily **journaling** with AI-driven sentiment and emotion analysis
- 🌈 Mood tracking with beautiful heatmaps
- 🧠 Personalized **CBT-based nudges** for reflection and habit change
- 📈 Mental health insights over time
- 🛟 Optional peer support and emergency contacts

This empowers students to reflect, express, and grow emotionally in a **private, stigma-free** space.

## ✨ Features

- ✅ AI-based journaling with NLP feedback
- ✅ Mood check-ins with emotion sliders
- ✅ Personalized micro-nudges based on Cognitive Behavioral Therapy (CBT)
- ✅ Mood trends and heatmaps
- ✅ Sentiment + emotion analysis on journal entries
- ✅ Optional: anonymous peer circles for shared support
- ✅ Secure, private, and easy to use

## 📈 Impact

Helps students build emotional self-awareness

Provides low-cost, scalable mental health support

Can integrate into college portals or ed-tech platforms

Promotes early intervention and healthy emotional habits

## ⚙️ Tech Stack

| Layer       | Technology                         |
|------------|-------------------------------------|
| Frontend    | React Native (mobile-first)        |
| Backend     | Flask (REST API)                   |
| Database    | SQLite (development), PostgreSQL (prod) |
| NLP Models  | HuggingFace Transformers / OpenAI API |
| Sentiment   | DistilBERT / VADER for emotion detection |
| Auth        | Firebase Authentication            |





## 🛠️ Setup & Run Instructions

### Backend (Flask)
```bash
cd backend
pip install -r requirements.txt
python app.py
